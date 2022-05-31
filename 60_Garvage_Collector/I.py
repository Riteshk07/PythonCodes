import time
class A :
    def __init__(self):
        print("Object initialized")

    def __del__(self):
        print ("Object about to delete")
print("++++++++++++++++")

x = A()
y =A()
z= A()
time.sleep(3)
print("++++++++++++++++")
del y
time.sleep(3)
print("################")