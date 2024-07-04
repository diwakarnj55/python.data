class First:
    def one(self):
        print("first class")
class Second(First):
    def two(self):
        print("Second class")
class Fourth:
    def four(self):
        print("Fourth class")
class Third(Second,Fourth):
    def three(self):
        print("Third class")
x=Third()
x.one()
x.two()
x.three()
x.four()