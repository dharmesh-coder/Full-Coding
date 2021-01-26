import math
def isPrime(num):
    if(num==1):
        return False
    if(num==2):
        return True
    if(num%2==0):
        return False

    i = 3
    while(i<math.sqrt(num)+1):
        if num%i==0:
            return False
        i += 2
    return True

t=int(input())
ans=[]
for i in range(t):
      n=int(input())
      cnt=0
      for j in range(3,n+1,2):
            if(isPrime(2+j) and 2+j<=n):
                  cnt+=1
      ans.append(cnt)
      
for i in ans:
      print(i)