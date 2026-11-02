class Employee:
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


e1 = Employee ("shubham", 19, 20000)
e2 = Employee ("Rohit", 23, 35000)

e1.display()
e2.display()