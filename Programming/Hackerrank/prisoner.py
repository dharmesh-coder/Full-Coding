t=int(input())
a=[]
for i in range(t):
    n,m,s=[int(x) for x in input().split()]
    m=m%n
    ans=(s-1)+m
    if (ans>n):
        a.append(ans%n)
    else:
        a.append(ans)
for i in a:
    print(i)
