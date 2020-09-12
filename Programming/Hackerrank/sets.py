n,m=input().split()
n=int(n)
m=int(m)
total=0
a = list(map(int,input().strip().split()))[:n]
b = list(map(int,input().strip().split()))[:m]
c=[]
for i in range(max(a),(min(b)+1)):
    count=0
    for j in range(len(a)):
        if (i%a[j]==0):
            count+=1
        if (count==n):
            c.append(i)

for i in range(len(c)):
    count=0
    for j in range(len(b)):
        if (b[j]%c[i]==0):
            count+=1
        if (count==m):
            total+=1
print(total)
