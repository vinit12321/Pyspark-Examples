class Bird:
    def __init__(self) -> None:
        print("I am Bird class.")
    
    
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("Many Birds can fly ")


class Sparrow(Bird):

    def intro(self):
        Bird.intro(self)
        print("Hey i am sparrow")
    

    def flight(self):
        print("I can fly")


class ostrich(Bird):
    def intro(self):
        return super().intro()
    
    def flight(self):
        return super().flight()


if __name__=='__main__':
    b1=Bird()
    b1.intro()
    b1.flight()
    s1=Sparrow()
    s1.intro()
    s1.flight()
