t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if(n<2020):
        ans.append("NO")
    else:
        found=False
        for i in range(int(n/2020)+1):
            for j in range(int(n/2020)+1):
                if((i*2020)+(j*2021)==n):
                    found=True
                    break
            if(found):
                break
        if(found):
            ans.append("YES")
        else:
            ans.append("NO")
for i in ans:
    print(i)