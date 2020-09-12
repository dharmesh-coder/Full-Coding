 repeat {    cat("Enter a no of choice -press 0 to terminate")
   x=scan(n=1)
   if (x==0) {
   break
   }
   sum=0
    while(x>0) {
    a=x%%10
    sum=sum+a
    x=x%/%10
    }
    cat("The sum of digits is ",sum)
 
 }