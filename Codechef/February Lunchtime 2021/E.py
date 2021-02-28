t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    s=set()
    
    ans.append(len(s))
for i in ans:
    print(i)
