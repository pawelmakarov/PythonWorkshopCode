# from Point import Point
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self == other

class ColorPoint(Point):
    def __init__(self, x=0, y=0, msg="White"):
        Point.__init__(self, x, y)
        self.msg = msg
    def __str__(self):
        return "Color: {0}, Point: {1}".format(self.msg, Point.__str__(self))
    # def __eq__(self, other):
    #     #implementation
    #     pass
    # def __ne__(self, other):
    #     #implementation
    #     pass

if __name__ == '__main__':
    a = ColorPoint(2.3, 3.2, "Black")
    b = ColorPoint(2.3, 3.2, "with")

    print(a)
    print(b)

    if a == b:
        print("equal")
    else:
        print("not equal")
