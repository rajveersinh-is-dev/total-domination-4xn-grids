"""Compute total domination numbers for grids and write a CSV table."""

import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.dp_4xn import total_domination_dp, formula_4xn

OUT = os.path.join("data", "values_4xn.csv")


def main():
    os.makedirs("data", exist_ok=True)
    with open(OUT, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "gamma_t_4xn", "formula"])
        for n in range(1, 101):
            value = total_domination_dp(4, n)
            writer.writerow([n, value, formula_4xn(n) if n >= 4 else ""])
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
