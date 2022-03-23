n=int (input ("Enter Number: "))
a = 1
for i in range(n):
    print("   "*((n-i-1))+"* "*(i+a))    
    a+=2