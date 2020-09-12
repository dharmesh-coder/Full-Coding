repeat {
print("Enter the year - press 0 to terminate")
y=scan(n=1)
if (y==0) {
break
}
daycode=(y+as.integer((y-1)/4)-as.integer((y-1)/100)+as.integer((y-1)/400))%%7
daycode=daycode+1
day=switch(daycode,"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
cat(day)
}