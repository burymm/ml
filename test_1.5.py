class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return self.capacity >= v + self.count

    def add(self, v):
        if (self.can_add(v)):
            self.count += v


x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)

print(x.count)