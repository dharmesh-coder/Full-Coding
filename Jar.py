string=input()
ans=""
ca=ce=ci=co=cu=0
for i in string:
    if (i=="a" or i=="A"):
        ca+=1
    elif (i=="e" or i=="E"):
        ce+=1
    elif (i=="i" or i=="I"):
        ci+=1
    elif (i=="o" or i=="O"):
        co+=1
    elif (i=="u" or i=="U"):
        cu+=1
    else:
        ans=ans+i
print("a:"+str(ca))
print("e:"+str(ce))
print("i:"+str(ci))
print("o:"+str(co))
print("u:"+str(cu))
print(ans)