x=scan(n=1)
n=scan(n=1)
if (x>=1 && x<=10 && n>=1 && n<=100) {
   a=(x**2)-x-n
   b=x-1
   c=floor(a/b)
   if (c%%2==0) {
       print("It is even")
   } else {
       print("It is odd")
   }
}