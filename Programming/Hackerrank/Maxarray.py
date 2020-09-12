l = list(map(int,input().strip().split()))[:5] 
l.sort()
Max=0
Min=0
for i in range(0,len(l)-1):
    Min=Min+l[i]
for i in range(1,len(l)):
    Max=Max+l[i]
print(Min,Max)