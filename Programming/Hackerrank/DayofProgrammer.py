def checkYear(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False

y=int(input())
if (y>=1700 and y<=1917):
    if (y%4==0):
        s1="12.09."+str(y)
        print(s1)
    else:
        s1="13.09."+str(y)
        print(s1)
elif (y==1918):
    print("26.09.1918")
else:
    if (checkYear(y)):
        s1="12.09."+str(y)
        print(s1)
    else:
        s1="13.09."+str(y)
        print(s1)