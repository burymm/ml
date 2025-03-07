    class Buffer:
        def __init__(self, *args):
            self.list = list(args)
            self.checkAndUpddate()

        def add(self, *args):
            self.list.extend(list(args))
            self.checkAndUpddate()

        def get_current_part(self):
            return(self.list)

        def checkAndUpddate(self):
            if len(self.list) >= 5:
                sum = 0;
                for i in range(5):
                    sum += self.list[i]
                print(sum)
                self.list = self.list[5:]
                self.checkAndUpddate()


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]