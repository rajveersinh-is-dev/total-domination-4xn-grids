"""Dynamic programming (transfer matrix) for total domination on 4 x n grids.

The state is the pair of selected-vertex masks of the last two columns.
This finite-state DP computes the minimum size of a total dominating set
for a 4-row grid with n columns in O(n * 2^(2m) * 2^m) time.
"""

from typing import Optional


def vertical_neighbors(mask: int, m: int) -> int:
    """Return a mask of rows in a column that have a selected vertical neighbour."""
    return ((mask << 1) & ((1 << m) - 1)) | (mask >> 1)


_dp_states_cache: dict[int, list[list[int]]] = {}
_dp_transitions_cache: dict[int, list[list[int]]] = {}


def total_domination_dp(m: int, n: int) -> Optional[int]:
    """Minimum size of a total dominating set of P_m x P_n via column DP."""
    if m <= 0 or n <= 0:
        return 0

    m_states = 1 << m
    full = m_states - 1
    infinity = 10**9

    if m not in _dp_states_cache:
        bc = [q.bit_count() for q in range(m_states)]
        dp = [infinity] * (m_states * m_states)
        for s in range(m_states):
            dp[s] = bc[s]
        _dp_states_cache[m] = [dp]

        vn = [vertical_neighbors(c, m) for c in range(m_states)]
        transitions: list[list[int]] = [[] for _ in range(m_states * m_states)]
        for p in range(m_states):
            for c in range(m_states):
                d_cur = vn[c] | p
                valid_qs = [q for q in range(m_states) if (d_cur | q) == full]
                transitions[p * m_states + c] = valid_qs
        _dp_transitions_cache[m] = transitions

    states = _dp_states_cache[m]
    transitions = _dp_transitions_cache[m]

    if len(states) < n:
        bc = [q.bit_count() for q in range(m_states)]
        for _ in range(len(states), n):
            dp = states[-1]
            newdp = [infinity] * (m_states * m_states)
            for pc in range(m_states * m_states):
                cost = dp[pc]
                if cost != infinity:
                    c = pc % m_states
                    c_m = c * m_states
                    for q in transitions[pc]:
                        ncost = cost + bc[q]
                        idx = c_m + q
                        if ncost < newdp[idx]:
                            newdp[idx] = ncost
            states.append(newdp)

    dp = states[n - 1]

    best = infinity
    vn = [vertical_neighbors(c, m) for c in range(m_states)]
    for pc in range(m_states * m_states):
        cost = dp[pc]
        if cost != infinity:
            p = pc // m_states
            c = pc % m_states
            d_last = vn[c] | p
            if d_last == full and cost < best:
                best = cost
    return None if best == infinity else best


def formula_4xn(n: int) -> int:
    """Conjectured/closed form for the 4 x n total domination number (n >= 4)."""
    constants = {0: 10, 1: 4, 2: 8, 3: 12, 4: 6}
    return (6 * n + constants[n % 5]) // 5


if __name__ == "__main__":  # pragma: no cover
    bad = []
    for _n in range(4, 501):
        _value = total_domination_dp(4, _n)
        if _value != formula_4xn(_n):
            bad.append((_n, _value, formula_4xn(_n)))
    print("checked n=4..500; discrepancies:", bad)
