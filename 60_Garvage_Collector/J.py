import time
class A :
    def __init__(self):
        print("Object initialized")

    def __del__(self):
        print ("Object about to delete")
print("++++++++++++++++")

x = [A(), A(), A()]
time.sleep(3)
print("++++++++++++++++")
# x = None
del x
time.sleep(3)
print("################")