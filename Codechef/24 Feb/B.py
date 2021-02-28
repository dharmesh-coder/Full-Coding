t=int(input())
ans=[]
for i in range(t):
    n,k=[int(x) for x in input().split()]
    a=list(map(int,input().strip().split()))[:k]
    for i in range(n):
        score=0
        s=input()
        for j in range(len(s)):
            if(s[j]=='1'):
                score+=a[j]
        ans.append(score)
for i in ans:
    print(i)
