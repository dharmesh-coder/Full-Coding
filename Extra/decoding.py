x=int(input())
a=str(x)
cnt=1
for i in range(len(a)):
    if (a[i]=='1' and i+1!=len(a)):
        cnt+=1
    if (a[i]=='2'):
        if (i+1!=len(a)):
            if (int(a[i+1])<7):
                cnt+=1
print(cnt)
    
