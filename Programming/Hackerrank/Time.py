s=input()
if (s[8:10]=="PM"):
    if (s[0:2]=="12"):
        print(s[0:8])
    else:
        a=int(s[0:2]) + 12
        b=str(a)
        print(b+s[2:8])
else:
    if (s[0:2]=="12"):
        print('00'+s[2:8])
    else:
        print(s[0:8])