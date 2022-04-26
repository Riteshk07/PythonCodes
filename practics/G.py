x="aaabbbbccccdddddaaaccc"
l = len(x)
count =0
y = 0 
i=x[0]
result= ""
def pro():
    global result
    global i
    global y
    global count 
    global l
    if y<l:
        pro()
        if i==x[y]:
            count +=1
            y += 1
        else :
            result+= str(count)+ i
            count =0
            i = x[y]
    return result

s=pro()
print(s+str(count)+i)

