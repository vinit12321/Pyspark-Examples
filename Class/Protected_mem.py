class Base:
    """
    Created Base class which contains protected members.
    """
    def __init__(self) -> None:
        self._a=10
    

    def getA(self):
        print(self._a)
    


class Derrived(Base):
    def __init__(self) -> None:
        Base.__init__(self)
        print("Calling Protected member from the Base Class",self._a)

        # Modify the Protected varibales.
        self._a=5
        print("Calling modified protected variable from outside of class",self._a)

    def getA(self):
        print("Accessing Value from Derrived Class",self._a)


if __name__=='__main__':
    # Created objects
    obj1=Derrived()

    obj2=Base()


    print("Accessing protected member of obj1: ", obj1._a)
    
    # Accessing the protected variable outside
    print("Accessing protected member of obj2: ", obj2._a)


    print("Calling Function",obj1.getA())