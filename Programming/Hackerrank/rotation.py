n,k,q=[int(x) for x in input().split()]
a=list(map(int,input().strip().split()))[:n]
indi=[]
ans=[0]*n
for i in range(q):
    p=int(input())
    indi.append(p)
k=k%n
for i in range(n):
    ans[n-1-i]=a[n-i-k-1]  
for i in indi:
    print(ans[i])
    