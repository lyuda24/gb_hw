class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self, weight1sq_m=0.025, thick=5):
        weight = self._length * self._width * weight1sq_m * thick
        print(f'Масса асфальта, необходимого для покрытия всей дороги = {int(weight)} т.')


r = Road(5000, 20)
r.weight()
