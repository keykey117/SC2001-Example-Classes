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
# S = [10, 50, 100, 200, 300, 400, 500, 1000]
# arrs = generatedata(50000, 50000, 10000)
# comparison = {}
# for s in S:
#     for arr in arrs:
#         print("sorting..")
#         count = 0
#         hybridsort(arr, 50)
#         comparison[s] = count
# print(comparison)

#c(iii)
result3={}
result4={}
result5={}
result6={}
result7={}
arrs= generatedata(1,pow(10,7),1000)

for S in range(1,100+1):
    count=0
    hybridsort(arrs[3], S)
    result3[S] = count
print("sorted "+ str(3))
for S in range(1,100+1):
    count=0
    hybridsort(arrs[4], S)
    result4[S] = count
print("sorted "+ str(4))
for S in range(1,100+1):
    count=0
    hybridsort(arrs[5], S)
    result5[S] = count
print("sorted "+ str(5))
for S in range(1,100+1):
    count=0
    hybridsort(arrs[6], S)
    result6[S] = count
print("sorted "+ str(6))
# for S in range(1,100+1):
#     count=0
#     hybridsort(arrs[7], S)
#     result7[S] = count
# print("sorted "+ str(7))

import json
with open('c3_3.txt', 'w') as file:
     file.write(json.dumps(result3))
with open('c3_4.txt', 'w') as file:
     file.write(json.dumps(result4))
with open('c3_5.txt', 'w') as file:
     file.write(json.dumps(result5))
with open('c3_6.txt', 'w') as file:
     file.write(json.dumps(result6))
# with open('c3_7.txt', 'w') as file:
#      file.write(json.dumps(result7))

#graph plotting X is S, Y is key comparisons
S_values=list(result3.keys())
keyComparisons=list(result3.values())
import matplotlib.pyplot as plt
plt.plot(S_values, keyComparisons)
plt.show()