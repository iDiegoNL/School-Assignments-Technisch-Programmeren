class Punt:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


p1 = Punt()
print("({} , {})".format(p1.x, p1.y))

p2 = Punt(3.5, 5.0)
print("({} , {})".format(p2.x, p2.y))
