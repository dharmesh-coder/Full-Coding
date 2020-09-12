n=int(input())
s=input()
c1=0
c2=0
total=0
for i in range(len(s)):
    if (s[i]=='U'):
        c1+=1
    else:
        c2+=1
    if (c1-c2==0 and (s[i])=='U'):
        total+=1
print(total)