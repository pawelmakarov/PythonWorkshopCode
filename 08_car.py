class Point:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y
    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))
    def distance(self, other):
        from math import hypot
        return hypot(self.x - other.x, self.y - other.y)

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return (self.value)

class Car(object):
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self.capacity = 60
        self.amount = 40
        self.consumption = 5.5
    
    @property
    def capacity(self):
        return self.capacity
    def capacity(self, value):
        self.capacity = value
    @property
    def consumption(self):
        return self.capacity
    def consumption(self, value):
        self.consumption = value
    def __str__(self):
        return "({0}, {1}, {2})".format(self.name, self.location, self.amount)
    def describe(self):
        return "{0}".format(self.__class__.__name__)
    
    def goAuto(self, newLocation):
        #implementation
        pass
    
    def goTank(self, newAmount):
        #implementation
        pass

if __name__ == '__main__':
    a = Point()
    b = Point(3.2, 3.3)
    bmw = Car(a, "BMW")

    try:
        bmw.goAuto(b)
    except MyError as e:
        print(e)

    print(bmw)
    bmw.goTank(20)
    print(bmw)

    print("New capacity: {0}".format(bmw.capacity))
    print("New consumption: {0}".format(bmw.consumption))
