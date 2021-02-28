t=int(input())
ans=[]
for i in range(t):
    n,k=[int(x) for x in input().split()]
    if(k==0):
        ans.append(n)
    else:
        a=n%k
        ans.append(a)
for i in ans:
    print(i)