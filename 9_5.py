class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Заупск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')


s_1 = Pen("ручка")
s_1.draw()

s_2 = Pencil("карандаш")
s_2.draw()

s_3 = Handle("маркер")
s_3.draw()
