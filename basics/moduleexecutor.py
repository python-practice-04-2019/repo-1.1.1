import modulepoint as mp
from modulepoint import display as dis
from modulepoint import person1
p = mp.Point()
p.init(10,20)
print(p.x, p.y)

mp.show(p)
dis(p)

print(person1['age'])
print(mp.person1['age'])

listResult = dir(mp)
print(listResult)