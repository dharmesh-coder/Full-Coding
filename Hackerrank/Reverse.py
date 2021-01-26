a=input()
ans=""
i=len(a)-1
j=len(a)-1
while (i>0):
    if(a[i]==" "):
        ans=ans+" "+a[i+1:j+1]
        j=i-1
    i=i-1
ans=ans+" "+a[i:j+1] 
print(ans[1:len(ans)])
    