from abc import abstractmethod, ABC

class Car(ABC):

    @abstractmethod
    def Break(self):
        pass
    @abstractmethod  
    def engine(self):
        pass
        
    def chesis(self):
        print("Chesis is Applied")
    def Stearing(self):
        print("Stearing is Applied")
    def mirror(self):
        print("Mirror is Applied")
        
    def display(self):
        print(self)
        self.Break()
        self.engine()
        self.chesis()
        self.Stearing()
        self.mirror()
        print()

class SimpleCar(Car):
    def Break(self):
        print("Break is Applied")
        
    def engine(self):
        print("engine is Applied")
    
class SportsCar(Car):
    def Break(self):
        print("Hydrolic Break is Applied")
        
    def engine(self):
        print("8 cylinder Engine is Applied")
    
class LuxuryCar(Car):
    def Break(self):
        print("Hydrolic Break is Applied")
        
    def engine(self):
        print("Jet Engine is Applied")
        
x = SimpleCar()
y = SportsCar()
z = LuxuryCar()

x.display()
y.display()
z.display()