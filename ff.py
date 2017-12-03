# def sleepiest(L):
#     new_L = []
#     for a in L:
#         new_L.append((a, a.count('z')))
#     return sorted(new_L, key = lambda x: x[1], reverse = True)[0]
#
# x = 'zanyzzz penisface poopooop yard penisface penisface'
# y = x.split()
# print y.count('Penisface'.lower())
#
# def threshold(s, num):
#     new_L = []
#     for a in s:
#         if s.count(a.lower()) >= num:
#             if a not in new_L:
#                 new_L.append(a)
#     return new_L
#
# print threshold('Hello lol', 2)


class Random():
    is_guy = True

    def __init__(self, name, hair):
        self.name = name
        self.hair = hair

    def isready(self):
        self.isready = False
    def isSI(self):
        self.isready = True
        return self.isready

p = Random('Jack', 'brown')
print type(p)
print p.isready()
print p.isready
print p.is_guy
print type(p.is_guy)
print type(p.name)
print type(p.isSI())
print type(p.isready())
print p.isSI()
print p.name
print p
