# more arguments with self
class Point:
    def init(self, x, y):
        self.x = x
        self.y = y
p1=Point()
p1.init(10,20)
print(p1.x,p1.y)