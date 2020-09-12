def height1(n):
    a=0
    height=0
    while (a<=n):
        if (a%2==0):
            height+=1
        else:
            height=height*2
        a+=1
    return height

n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
for i in arr:
    print(height1(i))