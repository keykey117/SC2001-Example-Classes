from numpy import random

# Merge sort taught in lecture


def mergeSort(arr):
    n = 0
    m = len(arr) - 1
    midPoint = (n+m)//2
    if (m-n <= 0):
        return arr
    else:
        lArr = mergeSort(arr[:midPoint+1])
        rArr = mergeSort(arr[midPoint+1:])

    return merge(lArr, rArr)  # merge to handle 2 elements


def generatedata(min, max, x):
    inputData = []
    size = min
    while size <= max:
        print("generating..")
        arr = [random.randint(1, x) for _ in range(size)]
        inputData.append(arr)
        size *= 10
    return inputData


def insertionsort(arr):
    global count
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            count += 1
            if (arr[j] < arr[j-1]):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr


def merge(lArr, rArr):
    global count
    i = 0
    j = 0
    res = []
    while i <= len(lArr)-1 and j <= len(rArr)-1:

        count += 1
        if lArr[i] < rArr[j]:
            res.append(lArr[i])
            i += 1
        else:
            res.append(rArr[j])
            j += 1
    if (i != len(lArr)):
        res += lArr[i:]
    else:
        res += rArr[j:]

    return res


def hybridsort(arr, S):
    if (len(arr) <= S):
        return insertionsort(arr)
    midPoint = len(arr)//2
    lArr = hybridsort(arr[:midPoint], S)
    rArr = hybridsort(arr[midPoint:], S)
    return merge(lArr, rArr)


# c(i) S = 50
# arrs = generatedata(1000, 10000000, 1000)
# counter = {}
# count = 0
# for arr in arrs:
#     print("sorting..")
#     count = 0
#     hybridsort(arr, 50)
#     counter[len(arr)] = count
# print(counter)

# c(ii) n = 50000
S = [10, 50, 100, 200, 300, 400, 500, 1000]
arrs = generatedata(50000, 50000, 10000)
comparison = {}
for s in S:
    for arr in arrs:
        print("sorting..")
        count = 0
        hybridsort(arr, s)
        comparison[s] = count
print(comparison)
