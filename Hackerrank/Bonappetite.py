n,x=input().split(" ")
n=int(n)
x=int(x)
s = list(map(int,input().strip().split()))[:n]
total=int(input())
actual=(sum(s)-s[x])/2
if (total>actual):
    print(int(total-actual))
else:
    print("Bon Appetit")