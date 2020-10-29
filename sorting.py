n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if (l[min]>l[j]):
            min=j
    l[i],l[min]=l[min],l[i]
print(*l)



