# Hostile internal review

## Review 1: technical validity

- The DP enumerates all 2^4 column masks and checks total domination of each vertex in the previous column before advancing. Discrepancies with CP-SAT were zero for tested sizes.
- The formula is only claimed for n>=4; small cases are tabled separately.
- The lower bound is supported by computation, not by a hand-written discharging proof. This is a limitation for a pure mathematics venue but acceptable for a computational journal.

## Review 2: significance and suitability

- The result is a modest but exact contribution. It is suitable for a computational combinatorics paper in The Computer Journal.
- The manuscript must not claim a general formula for all m; only m=4 is resolved.

## Actions taken

- Restricted all asymptotic claims to n>=4.
- Added CP-SAT verification for small cases.
- Documented the lack of a human-readable lower-bound proof as a limitation.
