def countWays(n) :
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2
     
    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
    return res[n]
 
t=int(input())
ans=[]
for i in range(t):
    x=int(input())
    ans.append(countWays(x+1))
for i in ans:
    print(i,end="\n")