def pri(n):
    flag=True
    for i in range(2,int(n/2)):
        if(n%i==0):
            flag=False
            return flag
    return flag

n=int(input())
count=0
a=3
while True:
    if(n==0):
        print(0)
        break
    if(pri(a)):
        count+=1
        if(count==n):
            print(a)
            break
    a+=1