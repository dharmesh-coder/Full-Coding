n=int(input())
a=list(map(int,input().strip().split()))[:n]
for i in range(n//2+1):
    if (i<(n-i-1)):
        a[i],a[n-i-1]=a[n-i-1],a[i]
print(*a)