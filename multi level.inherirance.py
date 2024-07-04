class First:
    def one(self):
        print("first class")
class Second(First):
    def two(self):
        print("second class")
class Third(Second):
    def three(self):
        print("third class")
x=Third()
x.one()
x.two()
x.three()