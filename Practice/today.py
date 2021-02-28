def rem(n):
    a=str(n)
    i=len(a)
    if(i==1 and n!=0):
        return n
    while True:
        if(a[i-1]=="0" and a[i-2]=="0"):
            return rem(a[0:i-1])
        else:
            return a[0:i-1]
        i-=1
        if(i==0 and a[i]!=0):
            return a[i]
n=int(input())
x=n
count=1
while True:
    if(x==n):
        break
    x=x+1
    x=int(rem(x))
    if(x!=n):
        count+=1
    
print(count)