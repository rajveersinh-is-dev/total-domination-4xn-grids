from src.verify_formula import verify_4xn


def test_verify_4xn():
    bad = verify_4xn(10)
    assert not bad
