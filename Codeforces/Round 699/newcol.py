t=int(input())
ans=[]
for i in range(t):
    n,k=input().split()
    mou=list(map(int,input().strip().split()))[:n]
    if(mou==mou.sort(reverse=True)):
        ans.append(-1)
    sum=0


    


