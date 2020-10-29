a,b=[int(x) for x in input().split()]
m1=[]
m2=[]
for i in range(a):
    l=[int(x) for x in input().split()][:b]
    m1.append(l)
for j in range(a):
    l=[int(x) for x in input().split()][:b]
    m2.append(l)
m=[0]*b
ans=[m]*a
for i in range(a):
    for j in range(b):
        ans[i][j]=m1[i][j]-m2[i][j]
for i in range(a):
    for j in range(b):
        print(ans[i][j],end=" ")