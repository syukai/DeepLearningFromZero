class Man:
    def __init__(self, name):
        self.name = name
        print("Welcome " + self.name + "!")

    def hello(self):
        print("Hello " + self.name + "!")
    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
s = Man("Samantha")
m.hello()
s.hello()
m.goodbye()
s.goodbye()

