class Clothes:
    def __init__(self):
        pass

    def fabric_consumption(self):
        pass


class Coat:
    def __init__(self, size):
        self.size = size

    def fabric_consumption(self):
        fc = self.size/6.5 + 0.5
        return f'Расход ткани на пошив пальто {self.size} размера составит {fc:.2f}м.'


class Suit:
    def __init__(self, height):
        self.height = height

    def fabric_consumption(self):
        fc = 2 * self.height + 0.3
        return f'Расход ткани на пошив костюма на рост {self.height}м составит {fc:.2f}м.'


clothes1 = Coat(46)
print(clothes1.fabric_consumption())
clothes2 = Suit(1.80)
print(clothes2.fabric_consumption())
