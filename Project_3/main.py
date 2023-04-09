def knapsack(w, p, C, n):
    profit = list()
    for i in range(C+1):
        profit.append([0] * (n+1))
    for capacity in range(1, C+1):
        for item in range(1, n+1):
            # base case when there is only 1 item
            if (item == 1):
                profit[capacity][item] = (capacity // w[item-1]) * p[item-1]
            else:
                if (capacity < w[item-1]):
                    profit[capacity][item] = profit[capacity][item-1]
                else:
                    profit[capacity][item] = max(profit[capacity-w[item-1]][item] +
                                                 p[item-1], profit[capacity][item-1])
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
