#counting.R
vcount=0
str=readline(prompt="Enter any string")
n=nchar(str)
for(i in 1:n) {
ch=substr(str,i,i)
vowels=c('a','e','i','o','u','A','E','I','O','U')
for(j in 1:10) {
if(ch==vowels[j]) {
vcount =vcount+1
}
}
}
cat("No. of vowels in the given string is:",vcount)
