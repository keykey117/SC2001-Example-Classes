def knapsack(w, p, C, n):
    profit = list()
    for i in range(C+1):
        profit.append([0] * (n+1))
    for r in range(1, C+1):
        for c in range(1, n+1):
            profit[r][c] = profit[r][c-1]
            if (w[c-1] <= r):
                if (profit[r][c] < profit[r-w[c-1]][c-1] + p[c-1]):
                    profit[r][c] = profit[r-w[c-1]][c-1] + p[c-1]
    print(profit)
    return profit[C][n]


# part a
p1 = [7, 6, 9]
w1 = [4, 6, 8]
print(knapsack(w1, p1, 14, len(w1)))

# part b
p2 = [7, 6, 9]
w2 = [5, 6, 8]
print(knapsack(w2, p2, 14, len(w2)))
