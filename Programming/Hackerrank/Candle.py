n=int(input())
l = list(map(int,input().strip().split()))[:n]
a=max(l)
count=0
for i in range(0,len(l)):
    if (l[i]==a):
        count=count+1
print(count) 