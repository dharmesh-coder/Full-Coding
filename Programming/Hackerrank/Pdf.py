l = list(map(int,input().strip().split()))[:26]
string=input()
value=[]
for i in string:
    x=l[ord(i)-97]
    value.append(x)
print(max(value)*len(string))