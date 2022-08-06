from datetime import date
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    @classmethod
    def Age_Today(cls,name,year):
        return cls(name,date.today().year-year)
    
    @staticmethod
    def age_check(age):
        if age>=18:
            print("He is Adult")
        else:
            print("He is not Adult")


if __name__=='__main__':
    p=Person("Vinit",23)
    pt=Person.Age_Today('Vinit',2002)
    print(pt.age)
    print(p.age)
    #print(p.Age_Today("Vinit","1998"))
    print(p.age_check(2002))
