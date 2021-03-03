def cou(x):
    tot=1
    for i in range(1,int(x//2)+1):
        if(x%i==0):
            tot+=1
    return tot

t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if(n<6):
        ans.append(cou(n))
    else:
        while True:
            a=[]
            j=6
            while True:
                if(cou(j)==4 and n%j==0):
                    a.append(j)
                j+=1
                if(j==(n+1)):
                    break
                if(len(a)==2):
                    break
            if(len(a)==0):
                ans.append(cou(n))
                break
            elif(len(a)==1):
                n=n/a[0]
            elif(cou(a[0])<cou(a[1])):
                n=n/a[0]
            else:
                n=n/a[1]
            if(n<6):
                ans.append(cou(n))
                break  
for i in ans:
    print(i)


        