class Dog:
    def __init__(self) -> None:
        pass
    attr1='Charile'
    attr2='Rocky'
    def func1(self):
        print("I am attr1",self.attr1)
        print("I am attr2",self.attr2)


rod=Dog()
print(rod.attr1)
print(rod.attr2)
print(rod.func1())
