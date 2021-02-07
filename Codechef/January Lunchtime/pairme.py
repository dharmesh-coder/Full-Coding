t=int(input())
ans=[]
for i in range(t):
    a,b,c=input().split()
    a=int(a);b=int(b);c=int(c)
    if(a+b==c or a+c==b or b+c==a):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)