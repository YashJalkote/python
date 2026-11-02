class student:
    def __init__(self,name, age, roll_no, percentage):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.percentage = percentage

    def display(self):
        print("Name:", self.name)
        print("Age", self.age)
        print("Roll_No:", self.roll_no)
        print("Percentage:", self.percentage)

s1 = student("Yash", 18, 101, 90)
s1.display()