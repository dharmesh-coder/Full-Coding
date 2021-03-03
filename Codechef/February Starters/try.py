def cou(x):
    tot=1
    for i in range(1,(x//2)+1):
        if(x%i==0):
            tot+=1
    return tot
for i in range(121):
    if(cou(i)==4 and 120%i==0):
        print(i)