t=int(input())
ans=[]
for i in range(t):
    a,b=input().split()
    a=int(a)
    b=int(b)
    s=input()
    one=False
    two=False
    if(a<0):
        if(s.count('L')>=abs(a)):
            one=True
    else:
        if(s.count('R')>=a):
            one=True
    if(b<0):
        if(s.count('D')>=abs(b)):
            two=True
    else:
        if(s.count('U')>=b):
            two=True
    if(one and two):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)