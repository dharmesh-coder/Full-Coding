n=int(input())
l=list(map(int,input().strip().split()))
max1=0
for i in l:
    if(i>max1):
        max1=i
max2=0
for i in l:
    if (i != max1):
        if (i>max2):
            max2=i
print(max2)
