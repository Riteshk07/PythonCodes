from abc import abstractmethod, ABC
class A(ABC):
    @abstractmethod
    def pro(self):
        pass
        
    def info(self):
        print("Hello ji")
        
x = A()

# x.pro()
x.info()
# TypeError: Can't instantiate abstract class A with abstract method pro