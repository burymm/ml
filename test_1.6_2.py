import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, msg):
        super().append(msg)  
        return self.log(msg)


def test():
    z = LoggableList()
    z.append('Hello!')
    z.append('Good bye!')   
    
    
test()
