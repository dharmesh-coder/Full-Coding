t=int(input())
ans=[]
for i in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    a=list(map(int,input().strip().split()))[:n]
    b=[]
    for i in a:
        if(i%k!=0 or k/i!=2):
            b.append(i)
    if(len(b)==0 or sum(b)%k==0):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)
    