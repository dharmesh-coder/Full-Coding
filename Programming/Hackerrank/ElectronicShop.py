b,n,m=input().split()
b=int(b)
n=int(n)
m=int(m)
l1 = list(map(int,input().strip().split()))[:n]
l2 = list(map(int,input().strip().split()))[:m]
l3=[]
for i in l1:
    for j in l2:
        if (i+j<=b):
            l3.append(i+j)
if (len(l3)==0):
    print(-1)
else:
    print(max(l3))
