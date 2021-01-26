q=int(input())
s=[]
a=[]
for i in range(q):
    s = list(map(int,input().strip().split()))[:3]
    if (abs(s[0]-s[2])>abs(s[1]-s[2])):
        a.append("Cat B")
    elif(abs(s[0]-s[2])<abs(s[1]-s[2])):
        a.append("Cat A")
    else:
        a.append("Mouse C")
for i in range(len(a)):
    print(a[i],end="\n")    