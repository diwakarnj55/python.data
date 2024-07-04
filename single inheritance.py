class First:
    def one(self):
        print("First class")
class Second(First):
    def two(self):
        print("Second class")
x=Second()
x.one()
x.two()