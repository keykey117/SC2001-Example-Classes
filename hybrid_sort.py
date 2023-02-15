def insertionsort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if (arr[j]<arr[j-1]):
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
    return arr

def merge(lArr,rArr):
    i=0
    j=0
    res=[]
    while i <= len(lArr)-1 and j <= len(rArr)-1:
        if lArr[i] < rArr[j]:
            res.append(lArr[i])
            i += 1
        else:
            res.append(rArr[j])
            j += 1
    if (i!=len(lArr)):    
        res += lArr[i:] 
    else:
        res += rArr[j:]

    return res

def hybridsort(arr,S):
    if (len(arr)<=S):
        return insertionsort(arr)
    midPoint=len(arr)//2
    lArr=hybridsort(arr[:midPoint],S)
    rArr=hybridsort(arr[midPoint:],S)
    return merge(lArr,rArr)    

#generate array
arr=[1,2,3,3,2,1,5,1,3,5,7,8,9,1,2,4,8,6,8]
print(hybridsort(arr,2)) #S is 2= 2 element arrays- need to minus 1 i think