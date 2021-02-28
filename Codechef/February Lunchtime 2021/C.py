# cook your dish here
def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)

t=int(input())
ans=[]
for i in range(t):
    a,b=[int(x) for x in input().split()]
    for i in range( b-a,a+1):
        if(gcd(a,i)==1 and i+a>b):
            ans.append(i)
            break
for i in ans:
    print(i)
