class Cell:
    """Cell - клетка, slot - ячейка"""
    def __init__(self, slots):
        self.slots = slots

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __str__(self):
        return f'Клетка с количеством ячеек: {self.slots}'

    def __sub__(self, other):
        sub = self.slots - other.slots
        if sub > 0:
            return Cell(sub)
        else:
            return 'Вычитание невозможно'

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __floordiv__(self, other):
        return Cell(self.slots // other.slots)

    def __truediv__(self, other):
        return Cell(self.slots / other.slots)

    def make_order(self, slots_in_row):
        row = ''
        for i in range(int(self.slots / slots_in_row)):
            row += f'{"*" * slots_in_row} \n'
        row += f'{"*" * (self.slots % slots_in_row)}'
        return row


c1 = Cell(30)
c2 = Cell(20)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 // c2)
print(c1 / c2)
c3 = Cell(50)
print(c3.make_order(20))
