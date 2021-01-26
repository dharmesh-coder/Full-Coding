t=int(input())
ans=[]
for i in range(t):
    s=input()
    if(len(s)<=10):
        ans.append("NO")
        continue
    if (s[0] in "@#%&?" or s[len(s)-1] in "@#%&?"):
        ans.append("NO")
        continue
    lcnt=0
    scnt=0
    dcnt=0
    spc=0
    for i in range(len(s)):
        if(s[i].isalpha()):
            if(s[i].lower()==s[i]):
                scnt+=1
            else:
                if(i!=0 or i!=len(s)-1):
                    lcnt+=1
        if(s[i].isdigit()):
            dcnt+=1
        if(s[i] in "@#%&?"):
            spc+=1
    if(lcnt>=1 and scnt>=1 and dcnt>=1 and spc>=1):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)  
        

