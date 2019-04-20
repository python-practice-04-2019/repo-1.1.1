import math

# using 2 objects in python
class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def evaluate_distance(self, other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
        
p1 = Point()
p2 = Point()
p1.init(10, 20)
p2.init(30, 40)

print(
    p1.evaluate_distance(p2))
