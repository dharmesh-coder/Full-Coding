t=int(input())
ans=[]
for i in range(t):
      l,r=input().split()
      l=int(l)
      r=int(r)
      ans.append(2*(r-l)+1)
for i in ans:
      print(i)