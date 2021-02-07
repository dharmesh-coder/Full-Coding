n=int(input())
li=list(map(int,input().strip().split()))[:n]
p=int(input())
x=[]
ans=[]
for i in range(p):
	a,b=input().split()
	a=int(a)
	b=int(b)
	x.append([a,b])
for i in range(n):
	fund=li[i]
	ind=i+1
	for i in x:
		if(ind==i[0] or ind==i[1]):
			if(ind==i[0]):
				fund+=li[i[1]-1]
			else:
				fund+=li[i[0]-1]
	ans.append(fund)
print(max(ans))