s=input()
ans=""
sum=0
dec=False
for i in s:
    if (i.isdigit()):
        ans+=i
        dec=True
    elif(dec==True):
        sum = sum + int(ans)
        ans="0"
print(sum+int(ans))
        