class First:
    def one(self):
        print("first class")
class Second(First):
    def two(self):
        print("second class")
class Fourth:
    def four(self):
        print("fourth class")
class Third(Second,Fourth):
    def three(self):
        print("Third Class")
x=Third()
x.one()
x.two()
x.three()
x.four()

