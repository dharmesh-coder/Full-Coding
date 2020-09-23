def binary_search(arr, low, high, x):  
    while high >= low: 
        mid = low+((high-low)//2)
        if (arr[mid]==x):
            return mid
        if (arr[mid]>x):
            high=mid-1
        if (arr[mid]<x):
            low=mid+1
    return mid+1   
a=[1,2,3,4,5,6,7,8,10]
z=binary_search(a,0,len(a)-1,9)
print(z)
