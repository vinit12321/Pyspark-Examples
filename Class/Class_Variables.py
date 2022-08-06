class Person:
    x=100
    name="Vinit"
"""
Class stores all information inside the 
__dict__ dictionary.so that we can track the state.
"""
print(Person.__dict__)
print("Printing the value using direct access ",Person.x)
print("Using getattr",str(getattr(Person,'x')))

#Changing the class variables 

Person.name="VinitDabake"
Person.age="24"

print("Printing dictonary after the adding the few values")
print(Person.__dict__)

"""
Python first check for instance dictionary & then check it
for the class variable.
"""


p1=Person()
p2=Person()

print(p1.x,p2.x)
#adding instance varible,
p1.x=50
print(p1.x,p2.x)
print(p1.__dict__,p2.__dict__)