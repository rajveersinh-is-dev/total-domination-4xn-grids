"""Verification helpers for the 4 x n total domination formula."""

from src.dp_4xn import total_domination_dp, formula_4xn


def verify_4xn(limit: int = 500) -> list[tuple[int, int, int]]:
    """Return discrepancies between DP values and the closed form for n=4..limit."""
    discrepancies = []
    for n in range(4, limit + 1):
        value = total_domination_dp(4, n)
        expected = formula_4xn(n)
        if value != expected:
            discrepancies.append((n, value, expected))
    return discrepancies


if __name__ == "__main__":
    bad = verify_4xn(500)
    print("discrepancies:", bad)
    print("OK" if not bad else "FAILED")
PYEOF