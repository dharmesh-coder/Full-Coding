a=[1,2,3]
n=len(a)
temp=a[n-1]
for i in range(n-1,0,1):
    a[i]=a[i-1]
a[0]=temp
print(a)