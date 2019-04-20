class Point:
    pass


'''
Since our first class doesn't actually do anything, we simply use the pass keyword on the second line to indicate that no further action needs to be taken.
'''

p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 6
p2.y = 3
print(p1.x, p1.y)
print(p2.x, p2.y)
