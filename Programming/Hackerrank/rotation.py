n,k,q=[int(x) for x in input().split()]
a=list(map(int,input().strip().split()))[:n]
indi=[]
for i in range(q):
    p=int(input())
    a.append(p)
for i in range(k):
    temp=a[n-1]
    for i in range(n-1,1):
        a[i]=a[i-1]
    a[0]=temp
for i in indi:
    print(a[i])
    