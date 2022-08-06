"""
An abstract class can be considered as a blueprint for other classes. 
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
A class which contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation. 
While we are designing large functional units we use an abstract class. 
When we want to provide a common interface for different implementations of a component, we use an abstract class. 
"""

from abc import ABC,abstractmethod
from traceback import print_tb

from matplotlib.pyplot import cla
class Polygon(ABC):
    def type_cls(self):
        print("From Abstract Class")
    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):
    def no_of_sides(self):
        print("I have 3 sides")
    
    def type_cls(self):
        super().type_cls()
        print("From Inside of Class")

class Square(Polygon):
    def no_of_sides(self):
        print("I have 4 sides")


class  Pentagaon(Polygon):
    def no_of_sides(self):
        print("I have 5 sides")


if __name__=="__main__":
    R=Triangle()
    R.no_of_sides()
    P=Pentagaon()
    P.no_of_sides()
    R.type_cls()
