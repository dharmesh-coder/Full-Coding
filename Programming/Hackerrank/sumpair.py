n,k=input().split()
n=int(n)
k=int(k)
count=0
l = list(map(int,input().strip().split()))[:n]
for i in range(n):
    for j in range(i+1,n):
        if ((l[i]+l[k])%k==0):
            count+=1
print(count)