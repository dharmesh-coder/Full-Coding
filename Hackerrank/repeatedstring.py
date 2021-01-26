stri=input()
n=int(input())
count=0
l=len(stri)
for i in range(l):
    if(stri[i]=='a'):
        count+=1
count*=n//l
rem=n%l
if(rem==0):
    print(count)
else:
    for i in range(rem):
        if(stri[i]=='a'):
            count+=1
    print(count)
