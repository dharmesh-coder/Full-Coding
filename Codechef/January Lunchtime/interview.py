import math
t=int(input())
ans=[]
for i in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    a=list(map(int,input().strip().split()))[:n]
    solved=0
    x=False
    maxx=0
    for i in a:
        if(i>-1):
            solved+=1
        if(i>k):
            x=True
        if(i>maxx):
            maxx=i
    sc=math.ceil(n/2)
    if(solved<sc):
        ans.append("Rejected")
    elif(x):
        ans.append("Too Slow")
    elif(maxx<=1 and solved==n):
        ans.append("Bot")
    else:
        ans.append("Accepted")
for i in ans:
    print(i)
