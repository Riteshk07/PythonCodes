from abc import abstractmethod, ABC
class A(ABC):
    @abstractmethod
    def pro(self):
        pass
        
    def info(self):
        print("Hello ji")
        
class B(A):
    pass

x = B()
x.info()

# TypeError: Can't instantiate abstract class B with abstract method pro