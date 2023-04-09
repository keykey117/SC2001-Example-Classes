def knapsack(w, p, C, n):
    # initialise dp memory
    profit = list()
    for i in range(C+1):
        profit.append([0] * (n+1))

    for capacity in range(1, C+1):
        for item in range(1, n+1):
            profit[capacity][item] = profit[capacity][item-1]
            if (w[item-1] <= capacity):
                profit[capacity][item] = max(
                    profit[capacity][item], profit[capacity-w[item-1]][item] + p[item-1])
    for i in range(len(profit)):
        print(profit[i])
    print("Max profit: " + str(profit[C][n]))

    return profit[C][n]


# part a
w1 = [4, 6, 8]
p1 = [7, 6, 9]
knapsack(w1, p1, 14, len(w1))

# part b
w2 = [5, 6, 8]
p2 = [7, 6, 9]
knapsack(w2, p2, 14, len(w2))
