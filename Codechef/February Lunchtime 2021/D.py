NO_OF_CHARS = 256
 
 
def canFormPalindrome(st):
    count = [0] * (NO_OF_CHARS)
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
    odd = 0
 
    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            odd = odd + 1
 
        if (odd > 1):
            return False
    return True

t=int(input())
ans=[]
for i in range(t):
    s=input()
    if(canFormPalindrome(s)):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)