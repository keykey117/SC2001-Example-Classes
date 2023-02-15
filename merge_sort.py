#Merge sort taught in lecture
def mergesort(n,m):
    midPoint=(n+m)//2
    if (m-n<=0):
        return
    elif (m-n>1):
        mergesort(n,midPoint)
        mergesort(midPoint+1,m)
    merge(n,m) #merge to handle 2 elements
    return

def merge(n,m):
    #print(f'{arr[n]} to {arr[m]}')
    if (m-n<=0):
        return
    midPoint=(n+m)//2
    a=n #a and b are running indexes
    b=midPoint+1

    while (a<=midPoint and b <=m): #two halves not empty
        if (arr[a]<arr[b]):
            a+=1
            n+=1 #shift future place of where num will be inserted
        elif (arr[a]>arr[b]):
            temp=arr[b]
            arr[n+1:b+1] = arr[n:b]
            arr[n]=temp #plug back the temp variable
            
            b+=1
            n+=1 #accommodate b
            a+=1 #due to index shift 
            midPoint+=1 #due to index shift 
        else: #a==b
            if (a==midPoint and b==m): #not sure whats the reason for this
                break
            a+=1  # accommodate a
            n+=1
            
            temp=arr[b]  #accommodate b
            # while (i != n):
            #     arr[i] = arr[i-1]
            #     i -= 1
            arr[n+1:b+1] = arr[n:b]
            arr[n]=temp
            n+=1
            b+=1
            a+=1
            midPoint+=1
    return
        
arr=[1,2,3,1,2,5,3,4,1,2,3]
mergesort(0,len(arr)-1)
print(arr)