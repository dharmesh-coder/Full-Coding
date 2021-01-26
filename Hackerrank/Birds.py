n=int(input())
count=0
l = list(map(int,input().strip().split()))[:n]
type=[1,2,3,4,5]
count=[0,0,0,0,0]
for i in range(5):
    for j in range(n):
        if type[i]==l[j]:
            count[i]+=1
print(type[count.index(max(count))])