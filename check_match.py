from src.dp_4xn import total_domination_dp
from src.solve_td import total_domination_cpsat

for m in range(1, 6):
    for n in range(1, 6):
        dp = total_domination_dp(m, n)
        cp = total_domination_cpsat(m, n)
        if dp != cp:
            print(f"Mismatch at {m}x{n}: DP={dp}, CP={cp}")
print("Done checking.")
