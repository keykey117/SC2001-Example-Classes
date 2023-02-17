# Merge sort taught in lecture
def mergeSort(arr):
    n = 0
    m = len(arr) - 1
    midPoint = (n+m)//2
    if (m-n <= 0):
        return arr
    else:
        # print("lArr:", arr[:midPoint+1])
        lArr = mergeSort(arr[:midPoint+1])
        # print("rArr:", arr[midPoint+1:])
        rArr = mergeSort(arr[midPoint+1:])

    return merge(lArr, rArr)  # merge to handle 2 elements


def merge(lArr, rArr):
    i = 0
    j = 0
    res = []
    while i <= len(lArr)-1 and j <= len(rArr)-1:
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


arr = [1, 2, 3, 1, 2, 5, 3, 4, 1, 2, 3]
print(mergeSort(arr))
