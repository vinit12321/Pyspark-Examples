class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name is"+self.name)
        print("Age is {}".format(self.age))


class Employee(Person):
    def __init__(self, name, age, empid, designation) -> None:
        self.empid = empid
        self.designation = designation
        Person.__init__(self, name, age)

    def display(self):
        return super().display()

    def displayEmp(self):
        super().display()
        print("Emp id is {}".format(self.empid))
        print("Designation is {}".format(self.designation))


if __name__ == "__main__":
    ep = Employee("Vinit", 24, 'Q01154', 'SDE')
    print(ep.displayEmp())
