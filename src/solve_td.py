"""CP-SAT based exact solver for total domination numbers of grid graphs."""

# mypy: disable-error-code="attr-defined"


from typing import Optional

from ortools.sat.python import cp_model


def total_domination_cpsat(m: int, n: int, time_limit: float = 300.0) -> Optional[int]:
    """Return the total domination number of P_m x P_n using CP-SAT."""
    if m <= 0 or n <= 0:
        return 0
    if m > n:
        m, n = n, m

    model = cp_model.CpModel()
    x = {}
    for v in range(m * n):
        x[v] = model.NewBoolVar(f"x{v}")

    for i in range(m):
        for j in range(n):
            v = i * n + j
            nbrs = []
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nbrs.append(ni * n + nj)
            model.AddBoolOr([x[u] for u in nbrs])

    if m > 1:
        model.Add(
            sum(x[j] for j in range(n)) <= sum(x[(m - 1) * n + j] for j in range(n))
        )
    if n > 1:
        model.Add(
            sum(x[i * n] for i in range(m)) <= sum(x[i * n + n - 1] for i in range(m))
        )
    if m == n and m > 1:
        model.Add(sum(x[j] for j in range(n)) <= sum(x[i * n] for i in range(m)))

    model.Minimize(sum(x[v] for v in range(m * n)))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    if status == cp_model.INFEASIBLE:
        return None
    if status == cp_model.FEASIBLE:
        raise RuntimeError(f"CP-SAT returned FEASIBLE (suboptimal) for {m}x{n}")
    if status != cp_model.OPTIMAL:
        if status == cp_model.UNKNOWN:
            raise RuntimeError(f"CP-SAT timeout or unknown for {m}x{n}")
        raise RuntimeError(f"CP-SAT failed for {m}x{n}: {status}")
    return int(solver.ObjectiveValue())
