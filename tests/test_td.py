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


def test_cpsat_matches_dp_4x6():
    assert total_domination_cpsat(4, 6) == total_domination_dp(4, 6) == 8
