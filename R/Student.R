name <- readline(prompt ="Enter your name ")
stream <- readline(prompt ="Enter your stream ")
year <- readline(prompt ="Enter your year ")
Sub <- readline(prompt ="Enter your subject ")


attempt <- as.integer(readline(prompt = "How many attempts ?"))
sum <- 0

for (i in 1:attempt) {
     if(attempt>0) {
      grade <- as.integer(readline(prompt = "Enter marks "))
      sum <- as.integer(sum + grade)

      print(paste("Marks of attempt:",i,"-->",grade))
}
else {
     print("Please attempt the exam")
}
}
avggd <- as.integer(sum/attempt)
print(paste(name,"You have attempted",attempt," times","and your avg marks is ",avggd))