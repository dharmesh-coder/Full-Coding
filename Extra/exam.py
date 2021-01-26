n=int(input())
l=list(map(int,input().strip().split()))[:n]
ans=[0]
s=0
c=1
cnt=[]
for i in range(n-1):
    s=l[i]
    for j in range(i+1,n):
        s=s+l[j]
        c=c+1
        if (s>max(ans)):
            ans.append(s)
            cnt.append(c)
    s=0
    c=1
print(cnt[len(cnt)-1])
