c = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]



s=[]
a1=[]
for i in range(3):
    a=[int(j) for j in input().split()]
    s.append(a)
for i in c:
    b=0
    for j in range(3):
        for k in range(3):
            x=i[j][k]-s[j][k]
            b+=abs(x)
    a1.append(b)

print(min(a1))
