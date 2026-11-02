class num:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num %2 == 0:
            print("Even number")

        else:
            print("Odd number")

n = num(7)
n.check()