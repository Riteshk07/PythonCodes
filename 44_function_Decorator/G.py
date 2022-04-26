def greet(a,b):
   return a>b

def greet_more(func, lst):
    flag= True
    def xgreet():
        nonlocal flag
        nonlocal lst
        for i in range(len(lst)-1):
            if (func(lst[i] , lst[i+1])):
                flag = False
                return flag
        return flag
    return xgreet
x= [1,2,3,4,5,6]
y = greet_more(greet, x)
print("is list in Ascending order? ", y())