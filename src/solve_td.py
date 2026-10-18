"""CP-SAT based exact solver for total domination numbers of grid graphs."""


from ortools.sat.python import cp_model


def total_domination_cpsat(m: int, n: int, time_limit: float = 300.0) -> int:
    """Return the total domination number of P_m x P_n using CP-SAT."""
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
            model.Add(sum(x[u] for u in nbrs) >= 1)

    model.Minimize(sum(x[v] for v in range(m * n)))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(f"CP-SAT failed for {m}x{n}: {status}")
    return int(solver.ObjectiveValue())
