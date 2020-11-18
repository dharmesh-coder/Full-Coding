n=int(input())
a=list(map(int,input().strip().split()))[:n]
ans=[]
for i in range(n):
    x=a[i]
    y=a[x-1]
    ans.append(y)
for i in range(n):
    print((ans.index(i+1))+1)