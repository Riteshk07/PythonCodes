from abc import abstractmethod, ABC
class A(ABC):
    @abstractmethod
    def pro(self):
        pass
        
x = A()

x.pro()

# TypeError: Can't instantiate abstract class A with abstract method pro

