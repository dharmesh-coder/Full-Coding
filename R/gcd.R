gcd=function(a,b) {
   r=a%%b
   if (r==0) {
       return (b)
       } 
   else {
      gcd(b,r)
      }
}