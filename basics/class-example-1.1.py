class Point:
    def init(self):
        self.x = 2
        self.y = 5
    def display(self): # without self it will be an error regarding argument
        print("displaying")

p1 = Point()
p2 = Point()
p3 = Point()
p1.init() # initialize with default values for p1
p2.init()
Point.init(p3) # pass object as parameter and initialize as default values for p3
print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y)
