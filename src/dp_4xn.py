"""Dynamic programming (transfer matrix) for total domination on 4 x n grids.

The state is the pair of selected-vertex masks of the last two columns.
This finite-state DP computes the minimum size of a total dominating set
for a 4-row grid with n columns in O(n * 2^(2m) * 2^m) time.
"""

from typing import Optional


def vertical_neighbors(mask: int, m: int) -> int:
    """Return a mask of rows in a column that have a selected vertical neighbour."""
    res = 0
    for r in range(m):
        if (r > 0 and (mask >> (r - 1)) & 1) or (r < m - 1 and (mask >> (r + 1)) & 1):
            res |= 1 << r
    return res


def total_domination_dp(m: int, n: int) -> Optional[int]:
    """Minimum size of a total dominating set of P_m x P_n via column DP."""
    M = 1 << m
    full = M - 1
    INF = 10 ** 9

    # dp[(prev_mask, cur_mask)] = minimum cost after placing current column.
    dp = {}
    for s in range(M):
        dp[(0, s)] = bin(s).count("1")

    for _ in range(1, n):
        newdp = {}
        for (p, c), cost in dp.items():
            d_cur = vertical_neighbors(c, m) | p
            for q in range(M):
                if (d_cur | q) == full:
                    ncost = cost + bin(q).count("1")
                    key = (c, q)
                    if key not in newdp or ncost < newdp[key]:
                        newdp[key] = ncost
        dp = newdp
        if not dp:
            return None

    best = INF
    for (p, c), cost in dp.items():
        d_last = vertical_neighbors(c, m) | p
        if d_last == full and cost < best:
            best = cost
    return None if best == INF else best


def formula_4xn(n: int) -> int:
    """Conjectured/closed form for the 4 x n total domination number (n >= 4)."""
    constants = {0: 10, 1: 4, 2: 8, 3: 12, 4: 6}
    return (6 * n + constants[n % 5]) // 5


if __name__ == "__main__":
    bad = []
    for n in range(4, 501):
        value = total_domination_dp(4, n)
        if value != formula_4xn(n):
            bad.append((n, value, formula_4xn(n)))
    print("checked n=4..500; discrepancies:", bad)
