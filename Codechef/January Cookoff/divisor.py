t=int(input())
ans=[]
for i in range(t):
    d=int(input())
    a=6
    while True:
        found=False
        for j in range(2,int(a/2)):
            if(a%j==0):
                if(j-1>=d):
                    ans.append(a)
                    found=True
                    break
                else:
                    continue
        a+=1
        if(found):
            break
for i in ans:
    print(i)

