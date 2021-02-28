t=int(input())
ans=[]
for i in range(t):
    a=list(map(int,input().strip().split()))[:10]
    k=int(input())
    x=9
    dec=k
    while True:
        if(a[x]>0):
            dec=dec-a[x]
            if(dec<0):
                ans.append(x+1)
                break
            else:
                x-=1
        else:
            x-=1
for i in ans:
    print(i)
        