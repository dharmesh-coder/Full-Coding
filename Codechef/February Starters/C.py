t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    a.sort()
    x=a[n-1]
    y=a[n-2]
    x1=a[0]
    y1=a[1]
    dec1=x*y+max(x-y,y-x)
    dec2=x1*y1+max(x1-y1,y1-x1)
    if(dec1>dec2):
        ans.append(dec1)
    else:
        ans.append(dec2)
for i in ans:
    print(i)