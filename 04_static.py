class Mohican(object):
    static = 0
    last = None

    def __init__(self):
        # self.__class__ is a reference to the type of the current instance
        self.__class__.last = hex(id(self))
        self.__class__.static = self.__class__.static + 1
        self.seldID = self.__class__.static
    
    @classmethod
    def class_method(cls):
        cls.__name__ = 'Mohican New'
        return '{0} / {1} / {2} {3}'.format('@classmethod', cls.static, cls.last, cls.__name__)

    @staticmethod
    def static_method():
        return '{0} / {1} / {2} / {3}'.format('@staticmethod', Mohican.static, Mohican.last, Mohican.__name__)
    
    def __str__(self):
        return "seldID {0}, Address {1}, Last {2}".format(
            self.seldID, self.__class__.static, self.__class__.last)

if __name__ == "__main__":
    print(Mohican.static_method())

    n0 = Mohican()
    n1 = Mohican()
    n2 = Mohican()
    n3 = Mohican()
    n4 = Mohican()
    n5 = Mohican()

    print(n0)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)

    print(n0.class_method())
    print(n1.class_method())
    print(n2.class_method())
    print(n3.class_method())
    print(n4.class_method())
    print(n5.class_method())

    print(Mohican.static_method())
   