t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if(n%2==1):
        ans.append("YES")
    else:
        a=n
        while True:
            if(a%2==1):
                ans.append("YES")
                break
            a=a/2
            if(a==1):
                ans.append("NO")
                break           
for i in ans:
    print(i)



    