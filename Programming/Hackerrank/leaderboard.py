#a=[100,50,40,20,10]
#5
#a,0,4,5
def binary_search(arr, low, high, x):  
    while high >= low: 
        mid = low+((high-low)//2)
        if (arr[mid]==x):
            return mid+1
        if (arr[mid]>x):
            low=mid+1
        if (arr[mid]<x):
            high=mid-1
    return mid+1 

def uni(list1): 
    list_set = set(list1) 
    uniq = (list(list_set))
    return uniq

n=int(input())
a = list(map(int,input().strip().split()))[:n]
a=uni(a)
a.sort(reverse=True)
x=int(input())
b = list(map(int,input().strip().split()))[:x]
for i in range(0,x):
    z=binary_search(a,0,len(a)-1,b[i])
    if (b[i]>a[0]):
        print(1)
    elif (b[i]<a[len(a)-1]):
        print(len(a)+1)
    else:
        print(z)

    
