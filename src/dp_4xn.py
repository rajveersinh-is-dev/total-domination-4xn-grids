"""Dynamic programming (transfer matrix) for total domination on 4 x n grids.

The state is the pair of selected-vertex masks of the last two columns.
This finite-state DP computes the minimum size of a total dominating set
for a 4-row grid with n columns in O(n * 2^(2m) * 2^m) time.
"""

from typing import Optional


def vertical_neighbors(mask: int, m: int) -> int:
    """Return a mask of rows in a column that have a selected vertical neighbour."""
    return ((mask << 1) & ((1 << m) - 1)) | (mask >> 1)


_dp_states_cache = {}


def total_domination_dp(m: int, n: int) -> Optional[int]:
    """Minimum size of a total dominating set of P_m x P_n via column DP."""
    if n <= 0:
        return None

    M = 1 << m
    full = M - 1
    INF = 10 ** 9

    if m not in _dp_states_cache:
        bc = [bin(q).count("1") for q in range(M)]
        dp = {}
        for s in range(M):
            dp[(0, s)] = bc[s]
        _dp_states_cache[m] = [dp]

    states = _dp_states_cache[m]

    if len(states) < n:
        bc = [bin(q).count("1") for q in range(M)]
        vn = [vertical_neighbors(c, m) for c in range(M)]

        for _ in range(len(states), n):
            dp = states[-1]
            newdp = {}
            for (p, c), cost in dp.items():
                d_cur = vn[c] | p
                for q in range(M):
                    if (d_cur | q) == full:
                        ncost = cost + bc[q]
                        key = (c, q)
                        if key not in newdp or ncost < newdp[key]:
                            newdp[key] = ncost
            states.append(newdp)

    dp = states[n - 1]
    if not dp:
        return None

    best = INF
    vn = [vertical_neighbors(c, m) for c in range(M)]
    for (p, c), cost in dp.items():
        d_last = vn[c] | p
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
