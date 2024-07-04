class First:
    def one(self):
        print("First class")
class Second:
    def two(self):
        print("Second class")
class Third(First,Second):
    def three(self):
        print("Third class")
x=Third()
x.one()
x.two()
x.three()