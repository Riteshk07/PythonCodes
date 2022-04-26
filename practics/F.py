x="aaabbbbccccdddddaaaccc"
count =0
y = 0 
z = len(x)
i=x[0]
result= ""

while y<z :
    if i==x[y]:
        count +=1
        y += 1
    else :
        result+= str(count)+ i
        count =0
        i = x[y]

result +=str(count)+i
print(result)

