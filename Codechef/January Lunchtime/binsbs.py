t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    s=input()
    cnt1=0
    cnt0=0
    dec=False
    for i in s:
        if(int(i)==1):
            cnt1+=1
        else:
            cnt0+=1
    if(list(s)==sorted(s)):
        ans.append(0)
    elif(cnt1>cnt0):
        ans.append(cnt0)
    else:
        ans.append(cnt1)
for i in ans:
    print(i)
