class A:
    @abstractmethod
    def pro(self):
        pass
        
x = A()

x.pro()

# NameError: name 'abstractmethod' is not defined