string="aaaaaa"
a=string
count=0
l=[]
i=1
k=0
while(True):
    if(a==a[::-1]):
        l.append(a[i-1])
        count+=1
        a=string[i:]
        if (count==2):
            if (a==a[::-1]):
                l.append(a)
                break
            else: print("Impossible")
        else:
            continue
        i+=1
        k=k+1


    else:
        b=a[k:i]
        a=string[i:]
        if (a==a[::-1]):
            l.append(b)
            count+=1
        i=i+1
        if (count==3):
            break

print(l)


            
            

    
