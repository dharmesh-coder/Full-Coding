n=int(input())
f=int(input())
if (f==1 or f==n):
    print(0)
else:
    if (n%2==0):
        a=(f//2)
        b=int(n/2)-(f//2)
        print(min(a,b))
    else:
        if (f==n-1):
            print(0)
        else:
            a=f//2
            b=int(n/2)-(f//2)
            print(min(a,b))