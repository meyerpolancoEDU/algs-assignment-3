# CMPS 2200 Assignment 3
## Answers

**Name:**Meyer Polanco


Place all written answers from `assignment-03.md` here for easier grading.

1a) A greedy algorithm for this problem is to continuously choose the largest coin that you can less than the remaining distance to N. For example, if N = 13, first choose 8 (8 < 13 < 16), then choose 4 (4 < 5 < 8), then end with 1 (1 = 1).

1b) Greedy choice: Let 2^k be the largest coin <= the remaining amount N. In some optimal solution for N, there is at least one 2^k coin. Otherwise, that solution would make value at least 2^k using only coins of value <= 2^(k-1), which requires at least two coins; replacing those by one 2^k coin decreases the coin count, contradicting optimality unless a 2^k coin is used. So, choosing 2^k greedily is optimal

Optimal substructure: After taking one 2^k coin, the remainder is N' = N - 2^k. If the coins used for N' were not an optimal solution to N', we could replace them with an optimal solution and reduce the total number of coins, contradicting optimality. Therefore an optimal solution for R consists of a 2^k coin plus an optimal solution for N'.

Together, these imply the greedy algorithm is the optimal solution.

1c) The work and span would both be O(logn). We will need logn coins total in the worst case, because the coins have value 2^k. And, because choosing a coin is dependant on the previous coins you took (how much of N is remaining), span is also logn.

2a) Lets say Fortuito has coins for values 1, 8, 10 and we are trying to get value 16. Our greedy algorithm will direct us to choose a 10-coin, then 6 1-coins for a total of 7 coins. But the actual optimal solution is 2 8-coins.

2b) Let OPT(N) be the minimum number of coins needed to make N using the given denominations. If an optimal solution for N uses some first coin d (where d <= N), then the remaining amount N - d must itself be solved optimally; otherwise, replacing the remainder by a better solution would reduce the total coin count, contradicting optimality. Therefore OPT(N) = min over all d in D with d <= N of (1 + OPT(N - d)), with base case OPT(0) = 0. This proves the problem has optimal substructure.

2c) Bottom-up algorithm: Create an array OPT[0...N] with OPT[0] = 0. For a from 1 to N: set OPT[a] to the minimum, over coins d in D with d <= a, of 1 + OPT[a - d] (if no coin applies for a, then a is not makeable). If no coin applies for N, change is impossible; otherwise OPT[N] is the minimum number of coins.

Work is O(n). Span is O(n).
