class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, value):
        if value > 0:
            super().append(value)
        else:
            raise NonPositiveError()


x = PositiveList()
x.append(2)
x.append(3)
x.append(4)
x.append(5)
print(x)
x.append(-5)