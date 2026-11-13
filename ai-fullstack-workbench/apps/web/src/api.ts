import type { Dataset, Report } from "./types";

// W1/W2 learning layer. W3 replaces manual contract types using FastAPI OpenAPI + Orval.
async function json<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(path, init);
  if (!response.ok) {
    const body = await response.text();
    throw new Error("HTTP " + response.status + ": " + body.slice(0, 160));
  }
  return (await response.json()) as T;
}
export const loadDemo = (signal?: AbortSignal): Promise<Dataset> =>
  json<Dataset>("/api/demo", { signal });

export const preview = (data: Dataset, signal?: AbortSignal): Promise<Report> =>
  json<Report>("/api/reconcile/preview", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    signal,
    body: JSON.stringify(data),
  });
