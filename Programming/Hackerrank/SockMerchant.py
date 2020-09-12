def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq

n=int(input())
l = list(map(int,input().strip().split()))[:n]
d=CountFrequency(l)
sum=0
for i in d:
    if (d[i]>1):
        sum=sum+d[i]//2
print(sum)


