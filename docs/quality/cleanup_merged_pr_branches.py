"""One-time, tightly scoped merged-PR branch cleanup (dry-run by default).

Run locally with --plan for offline inventory. --apply is permitted ONLY on
GitHub Actions push/main with an authenticated GITHUB_TOKEN. It deletes only
explicit candidates after verifying the matching PR was merged to main,
the PR head matches the live branch, and (for legacy branches) the immutable
previously audited exact commit SHA still matches. Never force-pushes.
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO = "Xander-Xai/X-SuperPlay-FullStack-Learning-OS"
MAIN = "main"


@dataclass(frozen=True)
class Candidate:
    branch: str
    merged_pr: int
    expected_sha: str | None = None


CANDIDATES = (
    Candidate("audit/v4.2-knowledge-depth-20261114", 6,
              "5cb7dec8abccdd7fff12a506735715d149dcf8a1"),
    Candidate("docs/integrate-2026-fullstack-execution-20261114", 7,
              "eed94b70a68739c75ecc6aa155488649c077a0a8"),
    Candidate("audit/complete-fullstack-basics-20261114", 8,
              "f545402f505fbceaef757e823e8a1668decd26fc"),
    # This governance PR may be squash-merged, hence no self-referential SHA.
    # The actual branch SHA must equal GitHub's PR head SHA at cleanup time.
    Candidate("chore/governance-pr-branch-issue-20261115", 9),
)


def is_safe_to_delete(candidate: Candidate, live_sha: str, pr: dict) -> tuple[bool, str]:
    if candidate.branch == MAIN or not candidate.branch or candidate.branch.startswith("refs/"):
        return False, "ref_not_allowed"
    if pr.get("number") != candidate.merged_pr or not pr.get("merged") or not pr.get("merged_at"):
        return False, "pr_not_merged"
    head = pr.get("head") or {}
    base = pr.get("base") or {}
    head_repo = head.get("repo") or {}
    if (head.get("ref") != candidate.branch or head_repo.get("full_name") != REPO
            or base.get("ref") != MAIN):
        return False, "pr_repository_or_branch_mismatch"
    if live_sha != head.get("sha"):
        return False, "branch_has_new_commits_since_merge"
    if candidate.expected_sha is not None and live_sha != candidate.expected_sha:
        return False, "branch_sha_changed_since_audit"
    return True, "merged_pr_head_unchanged"


def api(method: str, path: str, token: str) -> dict:
    req = Request(
        "https://api.github.com/repos/" + REPO + "/" + path,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": "Bearer " + token,
            "User-Agent": "fullstack-learning-governance-branch-cleanup",
        },
    )
    with urlopen(req, timeout=15) as response:
        raw = response.read()
        return json.loads(raw) if raw else {}


def cleanup(token: str, apply: bool) -> list[dict]:
    results = []
    for candidate in CANDIDATES:
        branch_path = quote(candidate.branch, safe="/")
        try:
            live = api("GET", "git/ref/heads/" + branch_path, token)
        except HTTPError as exc:
            if exc.code == 404:
                results.append({"branch": candidate.branch, "status": "ALREADY_ABSENT"})
                continue
            raise
        pull = api("GET", f"pulls/{candidate.merged_pr}", token)
        sha = (live.get("object") or {}).get("sha", "")
        allowed, reason = is_safe_to_delete(candidate, sha, pull)
        if not allowed:
            # Hard failure: retain data and alert reviewer rather than guess.
            raise RuntimeError(f"REFUSED {candidate.branch}: {reason}")
        if apply:
            api("DELETE", "git/refs/heads/" + branch_path, token)
            try:
                api("GET", "git/ref/heads/" + branch_path, token)
            except HTTPError as exc:
                if exc.code != 404:
                    raise
            else:
                raise RuntimeError(f"VERIFY_FAILED: {candidate.branch} still present")
        results.append({
            "branch": candidate.branch,
            "pr": candidate.merged_pr,
            "status": "DELETED_AND_VERIFIED" if apply else "SAFE_TO_DELETE_DRY_RUN",
            "sha": sha,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", action="store_true", help="Offline candidate listing (default)")
    parser.add_argument("--dry-run", action="store_true", help="Query live refs and PRs, no deletion")
    parser.add_argument("--apply", action="store_true", help="Delete matching merged PR branches (GitHub Actions main push only)")
    args = parser.parse_args()
    if sum([args.plan, args.dry_run, args.apply]) > 1:
        parser.error("Choose at most one mode")
    if args.plan or not (args.dry_run or args.apply):
        print(json.dumps([vars(c) for c in CANDIDATES], indent=2))
        return 0
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        parser.error("GITHUB_TOKEN required for live audit")
    if args.apply and (
        os.getenv("GITHUB_REPOSITORY") != REPO
        or os.getenv("GITHUB_EVENT_NAME") != "push"
        or os.getenv("GITHUB_REF") != "refs/heads/main"
    ):
        parser.error("--apply allowed only in authenticated repository main push workflow")
    print(json.dumps(cleanup(token, args.apply), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
