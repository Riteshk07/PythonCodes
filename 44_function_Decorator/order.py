def getOrder_more(func):
    T=True
    def new_getOrder(iter, func1=lambda a,b:a>b ):
        nonlocal T
        for i in range(len(iter)-1):
            if (func1(iter[i+1] ,iter[i] )):
                T= False
                break

        if T==True:
            return "Iterable in Descending Order"
        elif func(iter,func1):
            return "Iterable in Ascending Order"
        else :
            return "Iterable not in Ascending Order nor Descending Order"
    return new_getOrder
# x= [1,2,3,4,5,6]
# x= [6,5,4,3,2,1]
# x= [1,4,5,6,2,3]

@getOrder_more
def get_order(iter, func=lambda a,b:a>b):
    flag= True
    for i in range(len(iter)-1):
        if (func(iter[i] , iter[i+1])):
            flag = False
            return flag
    return flag

# print(get_order(x))