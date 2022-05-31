from abc import abstractmethod, ABC
class A(ABC):
    @abstractmethod
    def pro(self):
        pass
        
    def info(self):
        print("Hello ji")
        
class B(A):
    def pro(self):
        print("Pro in B")

x = B()
x.pro()
x.info()