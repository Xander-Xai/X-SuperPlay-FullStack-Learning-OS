import { describe, expect, it } from "vitest";
import { amount, labels } from "./domain";

describe("reconciliation view", () => {
  it("distinguishes missing amount from zero", () => {
    expect(amount(null)).toBe("—");
    expect(amount("0.00")).toBe("0.00");
  });
  it("shows all statuses explicitly", () => {
    expect(Object.keys(labels)).toHaveLength(4);
    expect(labels.AMOUNT_MISMATCH).toContain("差异");
  });
});
