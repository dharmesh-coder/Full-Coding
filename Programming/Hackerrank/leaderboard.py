def binary_search(arr, low, high, x):  
    if high >= low: 
        mid = (high + low) // 2 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return mid

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
index=0
for i in range(0,x):
    
