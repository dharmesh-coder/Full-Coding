n=int(input())
s = list(map(int,input().strip().split()))[:n]
d,m=input().split()
d=int(d)
m=int(m)
r=[]
for i in range(0,n-m+1):
    r.append(sum(s[i:i+m]))
count=0
for i in r:
    if (i==d):
        count+=1
print(count)