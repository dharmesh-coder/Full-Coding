s,t=input().split() 
a,b=input().split() 
m,n=input().split()
s=int(s)
t=int(t)
a=int(a)
b=int(b)
m=int(m)
n=int(n)  
l1 = list(map(int,input().strip().split()))[:m]
l2 = list(map(int,input().strip().split()))[:n]
apple=0
orange=0
for i in range(len(l1)):
    if (a+l1[i]>=s and a+l1[i]<=t):
        apple+=1
for i in range(len(l2)):
    if (b+l2[i]>=s and b+l2[i]<=t):
        orange+=1
print(apple,"\n",orange)



