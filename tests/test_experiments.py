import os


def test_compute_values_matches_committed(monkeypatch, tmp_path):
    import experiments.compute_values

    # Redirect OUT to a temporary file
    temp_out = tmp_path / "values_4xn.csv"
    monkeypatch.setattr(experiments.compute_values, "OUT", str(temp_out))

    # Mock os.makedirs to not create "data" directory locally inside the temp path test
    original_makedirs = os.makedirs

    def mock_makedirs(name, exist_ok=False):
        if name == "data":
            return original_makedirs(temp_out.parent, exist_ok=exist_ok)
        return original_makedirs(name, exist_ok=exist_ok)

    monkeypatch.setattr(os, "makedirs", mock_makedirs)

    # Run the script
    experiments.compute_values.main()

    # Read the generated output in text mode
    with open(temp_out, "r", encoding="utf-8") as f:
        generated = f.read()

    # Read the committed output in text mode
    committed_path = os.path.join("data", "values_4xn.csv")
    with open(committed_path, "r", encoding="utf-8") as f:
        committed = f.read()

    assert (
        generated == committed
    ), "Committed data/values_4xn.csv is outdated or does not match."
