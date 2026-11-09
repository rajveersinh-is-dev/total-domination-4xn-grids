"""Verification helpers for the 4 x n total domination formula."""

import sys

from src.dp_4xn import formula_4xn, total_domination_dp


def verify_4xn(limit: int = 500) -> list[tuple[int, int, int]]:
    """Return discrepancies between DP values and the closed form for n=4..limit."""
    discrepancies = []
    for n in range(4, limit + 1):
        value = total_domination_dp(4, n)
        if value is None:
            raise ValueError(f"Total domination DP returned None for 4x{n}")
        expected = formula_4xn(n)
        if value != expected:
            discrepancies.append((n, value, expected))
    return discrepancies


if __name__ == "__main__":  # pragma: no cover
    bad = verify_4xn(500)
    print("discrepancies:", bad)
    if bad:
        print("FAILED")
        sys.exit(1)
    else:
        print("OK")
