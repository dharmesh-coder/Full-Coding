s=input()
t=input()
k=int(input())
a=len(s)
b=len(t)
c=min(a,b)
d=0
while True:
    if(s[0:d]!=t[0:d]):
        break
    d+=1
    if(d+1>c):
        break
ans=len(s)+len(t)-2*d
if(ans<=k):
    print("Yes")
else:
    print("No")
    
