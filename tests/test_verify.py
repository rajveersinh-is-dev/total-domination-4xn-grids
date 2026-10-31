from src.verify_formula import verify_4xn


def test_verify_4xn():
    bad = verify_4xn(10)
    assert not bad


def test_verify_4xn_discrepancy(monkeypatch):
    import src.verify_formula

    # Mock total_domination_dp to always return 0,
    # which will not match the expected formula output
    monkeypatch.setattr(src.verify_formula, "total_domination_dp", lambda m, n: 0)

    bad = verify_4xn(5)
    assert len(bad) > 0


def test_verify_4xn_value_none(monkeypatch):
    import pytest
    import src.verify_formula

    # Mock to return None and trigger ValueError
    monkeypatch.setattr(src.verify_formula, "total_domination_dp", lambda m, n: None)

    with pytest.raises(ValueError, match="Total domination DP returned None for 4x4"):
        src.verify_formula.verify_4xn(5)
