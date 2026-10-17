# Total Domination Number of 4 x n Grid Graphs

This repository contains the research code and manuscript for the exact total
domination number of $4 \times n$ grid graphs.

## Research question

What is the total domination number $\gamma_t(P_4 \square P_n)$ of the $4 \times n$
grid graph for all $n \ge 4$?

## Contribution

The exact formula is
\[
\gamma_t(P_4 \square P_n)=\frac{6n+C_{n \bmod 5}}{5},
\qquad
(C_0,C_1,C_2,C_3,C_4)=(10,4,8,12,6),
\]
for every $n \ge 4$. The formula is verified by a finite-state dynamic program for
all $n \le 500$ and by an independent CP-SAT solver for small cases.

## Repository layout

- `src/dp_4xn.py` — dynamic program for the $4 \times n$ total domination number.
- `src/solve_td.py` — CP-SAT based exact solver.
- `src/verify_formula.py` — verification of the closed form.
- `tests/` — automated tests.
- `experiments/compute_values.py` — generates `data/values_4xn.csv`.
- `data/values_4xn.csv` — computed values for $n=1,\dots,100$.
- `paper/` — LaTeX manuscript.
- `research/` — literature review, evidence ledger, hostile review, novelty assessment,
  journal selection, acceptance assessment, and limitations.

## Reproduction

```bash
python -m pytest -q
python experiments/compute_values.py
python -m src.verify_formula
```

The dynamic program checks the formula for $n=4,\dots,500$ in a few seconds.
The CP-SAT solver requires `ortools`.

## Status

The manuscript is a preprint-style research note. It has not been submitted,
peer-reviewed, or accepted by any journal. The formula is verified computationally;
a human-readable lower-bound proof is not included.

## License

MIT (see `LICENSE`).
