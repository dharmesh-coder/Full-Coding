a,b=input().split()
if(a=='R' or b=='R'):
	print("R")
elif(a=="J" or b=="J"):
	if(a=="J"):
		print(b)
	else:
		print(a)
else:
	print("D")