## Program: Divisibility
cat("Enter the limit for checking whole no")
num <- scan(n=1)

cat("Divisibility by what no")
dnum <- scan(n=1)

cat("Non-divisibility by what no")
ndnum <- scan(n=1)

cat("Desirable numbers within",num,"are following ones \n")

for (i in 1:num){
    if (i%%dnum==0 && ndnum!=0) {
              print(i)
}
)