t=int(input())
ans=[]
for i in range(t):
    s=int(input())
    q=list(map(int,input().strip().split()))[:s]
    sum1=0
    for j in range(s):
        e=list(map(int,input().strip().split()))
        if(len(e)==2):
            tot=e[1]
            sum1+=tot
        else:
            tot=sum(e)-e[0]-(len(e)-2)*q[j]
            sum1+=tot
    ans.append(sum1)
for i in ans:
    print(i)
