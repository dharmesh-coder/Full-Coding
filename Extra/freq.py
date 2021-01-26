n=int(input())
l=list(map(int,input().strip().split()))[:n]
mydict={}
for i in l:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1
print(mydict)
Keymax = max(mydict, key=mydict.get)