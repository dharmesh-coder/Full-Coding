x,a,y,b=input().split()
x=int(x)
y=int(y)
a=int(a)
b=int(b)
while(True):
    if(b>a or a==b):
        print("NO")
        break
    else:
        while(True):
            x=x+a
            y=y+b
            if (x==y):
                print("YES")
                break
            if (x>y):
                print("NO")
                break
    break