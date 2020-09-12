n=scan(n=1)
a=n
sum=0
while(a>0) {
  r=a %% 10
  sum=sum+(r**3)
  a=a%/%10
}
if (sum==n) {
print("The given number is Armstrong no")
} else {
print("The given number isn't armstrong")
}