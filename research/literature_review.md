---
title: "Total Domination Number of 4 x n Grid Graphs: An Exact Formula and Verified Computation"
author: "Rajveersinh Vishal Pardeshi"
---

# Research notes

## Search strategy

- Searched Google/academic sources for total domination numbers of grid graphs.
- Key prior work: Gravier, "Total domination number of grid graphs", Discrete Applied Mathematics 121 (2002), 119--128, which gives formulas for P_5 x P_n and P_6 x P_n.
- Used OR-Tools CP-SAT and a column-based dynamic program to compute exact values for 4 x n grids.

## Comparison with prior work

| Reference | Problem | Result | Relation to present work |
|---|---|---|---|
| Gravier (2002) | Total domination of P_m x P_n | Formulas for m=5,6; bounds for general m | Present work gives exact formula for m=4 |
| Henning and Yeo (2013) | General total domination | General bounds gamma <= gamma_t <= 2 gamma | Consistent with computed 4 x n values |
| Goncalves et al. (2011) | Ordinary domination of grids | Exact formula for large grids | Different domination variant |

## Novelty assessment

The exact formula for the total domination number of 4 x n grid graphs for all n >= 4,
with the periodic quasipolynomial
\[
\gamma_t(P_4 \times P_n)=\frac{6n+C_{n\bmod 5}}{5},
\qquad
C=(10,4,8,12,6),
\]
was not found in the searched literature. The result is supported by an independent
dynamic program checked up to n=500 and by CP-SAT for smaller cases.
