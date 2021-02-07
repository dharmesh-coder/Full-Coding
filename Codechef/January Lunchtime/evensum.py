t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    dec=sum(a)
    if(dec%2==0):
        ans.append(1)
    else:
        ans.append(2)
for i in ans:
    print(i)
