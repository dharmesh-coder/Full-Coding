t=int(input())
ans=[]
for i in range(t):
    m,h=[int(x) for x in input().split()]
    bmi=m/(h*h)
    if(bmi<=18):
        ans.append(1)
    elif(bmi<=24):
        ans.append(2)
    elif(bmi<=29):
        ans.append(3)
    else:
        ans.append(4)
for i in ans:
    print(i)