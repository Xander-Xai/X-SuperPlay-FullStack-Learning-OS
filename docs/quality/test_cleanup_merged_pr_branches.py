"""Offline branch deletion guard tests: never uses an actual GitHub token."""
import unittest

from cleanup_merged_pr_branches import (
    CANDIDATES, MAIN, REPO, Candidate, is_safe_to_delete,
)


def valid_pr(candidate: Candidate, sha: str) -> dict:
    return {
        "number": candidate.merged_pr,
        "merged": True,
        "merged_at": "2026-11-14T00:00:00Z",
        "head": {"ref": candidate.branch, "sha": sha, "repo": {"full_name": REPO}},
        "base": {"ref": MAIN},
    }


class BranchCleanupGateTest(unittest.TestCase):
    def test_all_candidates_are_named_distinct_and_not_main(self):
        names = [x.branch for x in CANDIDATES]
        self.assertEqual(len(names), len(set(names)))
        self.assertNotIn(MAIN, names)
        self.assertEqual([x.merged_pr for x in CANDIDATES], [6, 7, 8, 9])

    def test_known_merged_pr_head_can_delete(self):
        entry = CANDIDATES[0]
        self.assertEqual(
            is_safe_to_delete(entry, entry.expected_sha, valid_pr(entry, entry.expected_sha)),
            (True, "merged_pr_head_unchanged"),
        )

    def test_does_not_delete_nonmerged(self):
        entry = CANDIDATES[1]
        pr = valid_pr(entry, entry.expected_sha)
        pr["merged"] = False
        self.assertEqual(is_safe_to_delete(entry, entry.expected_sha, pr)[0], False)

    def test_does_not_delete_when_ref_advanced(self):
        entry = CANDIDATES[2]
        self.assertEqual(is_safe_to_delete(entry, "new-commit", valid_pr(entry, entry.expected_sha))[0], False)

    def test_does_not_delete_when_expected_immutable_sha_differs(self):
        entry = CANDIDATES[0]
        self.assertEqual(is_safe_to_delete(entry, "unexpected", valid_pr(entry, "unexpected"))[0], False)

    def test_does_not_delete_wrong_repository_or_target(self):
        entry = CANDIDATES[0]
        pr = valid_pr(entry, entry.expected_sha)
        pr["head"]["repo"]["full_name"] = "somebody/fork"
        self.assertEqual(is_safe_to_delete(entry, entry.expected_sha, pr)[0], False)
        pr = valid_pr(entry, entry.expected_sha)
        pr["base"]["ref"] = "other"
        self.assertEqual(is_safe_to_delete(entry, entry.expected_sha, pr)[0], False)

    def test_self_governance_branch_requires_pr_head_sha(self):
        entry = CANDIDATES[-1]
        self.assertEqual(is_safe_to_delete(entry, "sha-9", valid_pr(entry, "sha-9"))[0], True)
        self.assertEqual(is_safe_to_delete(entry, "sha-after-merge", valid_pr(entry, "sha-9"))[0], False)

    def test_never_delete_default_branch_or_arbitrary_ref(self):
        entry = Candidate(MAIN, 99)
        self.assertEqual(is_safe_to_delete(entry, "same", valid_pr(entry, "same"))[0], False)
        entry = Candidate("refs/heads/feature", 99)
        self.assertEqual(is_safe_to_delete(entry, "same", valid_pr(entry, "same"))[0], False)


if __name__ == "__main__":
    unittest.main()
