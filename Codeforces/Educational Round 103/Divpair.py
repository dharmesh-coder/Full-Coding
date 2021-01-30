t=int(input())
ans=[]
for i in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    if(n==1):
        ans.append(k)
    elif(n==k):
        ans.append(1)
    else:
        a=[1]*n
        sum=n
        i=n
        while True:
            if(sum%k==0):
                ans.append(a[i])
                break
            if(i==0):
                i=n
            a[i-1]+=1
            sum+=1
            i-=1
for i in ans:
    print(i)


    