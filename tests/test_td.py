from src.dp_4xn import total_domination_dp, formula_4xn
from src.solve_td import total_domination_cpsat


def test_dp_small_values():
    expected = {1: 2, 2: 4, 3: 4, 4: 6, 5: 8, 6: 8, 10: 14}
    for n, value in expected.items():
        assert total_domination_dp(4, n) == value


def test_formula_matches_dp():
    bad = []
    for n in range(4, 301):
        if total_domination_dp(4, n) != formula_4xn(n):
            bad.append(n)
    assert not bad, bad[:10]


def test_cpsat_matches_dp():
    for n in range(1, 16):
        assert total_domination_cpsat(4, n) == total_domination_dp(4, n)


def test_infeasible_grid():
    assert total_domination_cpsat(1, 1) is None
    assert total_domination_dp(1, 1) is None


def test_solve_td_timeout():
    import pytest

    with pytest.raises(RuntimeError):
        total_domination_cpsat(10, 10, time_limit=0.001)


def test_solve_td_unknown(monkeypatch):
    import pytest
    from ortools.sat.python import cp_model

    class MockSolver:
        def __init__(self):
            class DummyParameters:
                max_time_in_seconds = 300.0
                num_search_workers = 1

            self.parameters = DummyParameters()

        def Solve(self, model):
            return cp_model.UNKNOWN

    monkeypatch.setattr("src.solve_td.cp_model.CpSolver", MockSolver)

    with pytest.raises(RuntimeError, match="CP-SAT timeout or unknown"):
        total_domination_cpsat(2, 2)


def test_solve_td_model_invalid(monkeypatch):
    import pytest
    from ortools.sat.python import cp_model

    class MockSolver:
        def __init__(self):
            class DummyParameters:
                max_time_in_seconds = 300.0
                num_search_workers = 1

            self.parameters = DummyParameters()

        def Solve(self, model):
            return cp_model.MODEL_INVALID

    monkeypatch.setattr("src.solve_td.cp_model.CpSolver", MockSolver)

    with pytest.raises(RuntimeError, match="CP-SAT failed"):
        total_domination_cpsat(2, 2)


def test_dp_0_n():
    assert total_domination_dp(4, 0) == 0
    assert total_domination_dp(4, -1) == 0
    assert total_domination_dp(0, 4) == 0
    assert total_domination_dp(-1, 4) == 0


def test_dp_infeasible():
    # Test dp when no feasible configuration exists.
    # For a grid of size 1x1, there are no neighbors, so total domination is impossible.
    assert total_domination_dp(1, 1) is None


def test_cpsat_0_n():
    assert total_domination_cpsat(4, 0) == 0
    assert total_domination_cpsat(4, -1) == 0
    assert total_domination_cpsat(0, 4) == 0
    assert total_domination_cpsat(-1, 4) == 0


def test_dp_vs_cpsat_other_m():
    """Verify DP matches CP-SAT for grids with m != 4."""
    for m in [2, 3, 5]:
        for n in range(1, 6):
            assert total_domination_dp(m, n) == total_domination_cpsat(m, n)
