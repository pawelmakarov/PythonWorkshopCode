class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self, value):
        return self.value

class Pen:
    def __init__(self, paper, capacity=40):
        self.capacity = capacity
        self.amount = capacity
        self.space = paper
    def __str__(self):
        #implementation
        pass
    def refill(self, ink):
        #implementation
        pass
    def write(self, paper, msg):
        #implementation
        pass

class Paper:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.amount = 0
        self.freeSpace = self.capacity - self.amount
        self.content = ""
    def __str__(self):
        #implementation
        pass
    def show(self):
        #implementation
        pass
    def addContent(self, text, length):
        #implementation
        pass10

if __name__ == '__main__':
    paper = Paper()
    pen = Pen(paper)

    print(paper)
    print(pen)

    text = "It's time to deal for each of us..."
    try:
        pen.write(paper, text)
    except MyException as e:
        print(e.value)

    paper.show()

    print "Paper: {0}".format(paper)
    print "Pen {0}".format(pen)

    try:
        pen.refill(30)
    except MyException as e:
        print(e.value)
    print "Pen ", pen

    text = "A have a dream..."
    try:
        pen.write(paper, text)
    except MyException as a:
        print(a.value)
    paper.show()

    print "Paper: {0}".format(paper)
    print "Pen {0}".format(pen)
