n=int(input())
l = list(map(int,input().strip().split()))[:n]
count1=0
count2=0
for i in range(1,n):
    if (l[i]>high):
        high=l[i]
        count1+=1
    if (l[i]<low):
        low=l[i]
        count2+=1
print(count1,count2)
        
