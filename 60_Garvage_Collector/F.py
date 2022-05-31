import time
class A :
    def __init__(self):
        print("Object initialized")

    def __del__(self):
        print ("Object about to delete")
print("++++++++++++++++")

x = A()
print("################")
time.sleep(3)
# x = 12
x = None
print("++++++++++++++++")
time.sleep(3)
