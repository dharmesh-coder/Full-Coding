r,c=input().split()
r=int(r)
c=int(c)
mat=[]
for i in range(r):
    x = list(map(int,input().strip().split()))[:c]
    mat.append(x)
rsum=0
csum=0
for i in mat:
    a=0
    b=1
    while True:
        if(i[a]==6):
            if(i[b]!=6):
                rsum+=1
                a=b
                b+=1
            else:
                b+=1
        else:
            a+=1
            b+=1
        if(b==c):
            if(a<c-1):
                rsum+=1
                break
            elif(a==c-1 and i[a]==6):
                rsum+=1
                break
            else:
                break
for i in range(c):
    a=0
    b=1
    while True:
        if(mat[a][i]==6):
                if(mat[b][i]!=6):
                    csum+=1
                    a=b
                    b+=1
                else:
                    b+=1
        else:
            a+=1
            b+=1
        if(b==r):
            if(a<r-1):
                csum+=1
                break
            elif(a==r-1 and mat[a][i]==6):
                csum+=1
                break
            else:
                break
print(min(rsum,csum))
print(rsum,csum)



