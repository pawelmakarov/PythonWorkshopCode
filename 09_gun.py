class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return (self.value)

class Gun(object):
    def __init__(self, capacity=30, value=0):
        #initialize variable (capacity and value)
        pass

    @property
    def value(self):
        #implementation
        pass
    def value(self, newValue):
        #implementation
        pass
    def __str__(self):
        #implementation
        pass
    def refill(self, pistol):
        #implementation
        pass
    def shot(self):
        #implementation
        pass


if __name__ == '__main__':
    gun = Gun()
    print(gun)

    try:
        gun.shot()
    except MyException as e:
        print(e.value)

    try:
        gun.refill(50)
    except MyException as e:
        print(e.value)

    try:
        gun.shot()
    except MyException as e:
        print(e.value)

    try:
        gun.refill(25)
    except MyException as a:
        print(a.value)

    gun.value = 100500
    print(gun.value)
