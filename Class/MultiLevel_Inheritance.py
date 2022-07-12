

class Base1(object):
    def __init__(self,name) -> None:
        self.name=name
    
    def get_name(self):
        print(self.name)

    
class Child1(Base1):
    def __init__(self, name,age) -> None:
        self.age=age
        Base1.__init__(self,name)
    
    def get_age(self):
        print(self.age)
    


class GrandChild(Child1):
    def __init__(self, name, age,address) -> None:
        self.adddress=address
        Child1.__init__(self,name,age)

    def get_address(self):
        print(self.adddress)
    

if __name__=="__main__":
    g1=GrandChild("Vinit",27,"Virar")
    g1.get_name()
    g1.get_age()
    g1.get_address()
