n=int(input())
s = list(map(int,input().strip().split()))[:n]
total=[]
for i in s:
    count=1
    count1=0
    count2=0
    for j in range(len(s)):
        if (j!=(s.index(i)) and s[j]-i==0):
            count+=1
        if (j!=(s.index(i))):
            if ((s[j]-i)==1):
                count1+=1
            if ((s[j]-i)==(-1)):
                count2+=1
    total.append((max(count1,count2))+count)
print(max(total))



#