t=int(input())
ans=[]
for i in range(t):
    s=int(input())
    a=list(map(int,input().strip().split()))[:s]
    a.sort()
    ans.append(abs(a[0]-a[1])+abs(a[1]-a[s-1])+abs(a[0]-a[s-1]))
for i in ans:
    print(i)