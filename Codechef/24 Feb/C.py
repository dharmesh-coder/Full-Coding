t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    x=list(a)
    b=[0]*n
    x.sort(reverse=True)
    for i in range(n):
        b[a.index(x[i])]=i+1
    ans.append(b)
for i in ans:
    print(*i)

