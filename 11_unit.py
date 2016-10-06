class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self, value):
        print(self.value)

class Unit(object):
    def __init__(self, hitPoints=30, attack=10):
        #implementation
        pass

    def __str__(self):
        #implementation
        pass

    def ifDead(self):
        #implementation
        pass
        
    def doAttack(self, newUnit):
        #implementation
        pass

if __name__ == '__main__':
    unit1 = Unit(35, 10)
    unit2 = Unit(45, 5)

    print("Unit One: {0}".format(unit1))
    print("Unit Two: {0}".format(unit2))

    try:
        unit1.doAttack(unit2)
    except MyException as e:
        print(e.value)

    print("Unit One: {0}".format(unit1))
    print("Unit Two: {0}".format(unit2))

    try:
        unit2.doAttack(unit1)
    except MyException as e:
        print(e.value)

    print("Unit One: {0}".format(unit1))
    print("Unit Two: {0}".format(unit2))
