"""
Self:
Class methods must have an extra first parameter in the method definition.
We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.

"""


class Dog:
    def __init__(self) -> None:
        pass
    attr1 = 'Charile'
    attr2 = 'Rocky'

    def func1(self):
        print("I am attr1", self.attr1)
        print("I am attr2", self.attr2)


class Person:
    """
    This class contains the information about Person.
    """

    def __init__(self, name) -> None:
        self.name = name

    def say_hi(self):
        print("Hello,How are you ", self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


if __name__ == "__main__":

    pt = Person("Vinit")
    pt.say_hi()
    pt.set_age(24)
    print("Hello "+pt.name+" You are "+str(pt.get_age())+" years old")
