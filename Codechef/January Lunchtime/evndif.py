t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    cnt1=0
    cnt2=0
    for i in a:
        if(i%2==0):
            cnt1+=1
        else:
            cnt2+=1
    if(cnt1>cnt2):
        ans.append(cnt2)
    else:
        ans.append(cnt1)
for i in ans:
    print(i)