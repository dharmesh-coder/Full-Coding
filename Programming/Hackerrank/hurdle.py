n,k=input().split()
n=int(n)
k=int(k)
a = list(map(int,input().strip().split()))[:n]
if (max(a)>k):
    print(max(a)-k)
else:
    print(0)
