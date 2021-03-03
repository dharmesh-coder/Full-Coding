t=int(input())
ans=[]
for i in range(t):
    d,c=[int(x) for x in input().split()]
    a=list(map(int,input().strip().split()))[:3]
    b=list(map(int,input().strip().split()))[:3]
    a1=sum(a)
    b1=sum(b)
    y=a1+b1+2*d
    if(a1>=150 or b1>=150):
        if(a1>=150 and b1>=150):
            x=a1+b1+c
        else:
            x=a1+b1+c+d
    else:
        x=a1+b1+2*d
    if(x<y):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)
    