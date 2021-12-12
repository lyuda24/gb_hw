class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на{direction}!')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        print('Это городская машина!')
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости! Данная машина не может ехать со скоростью более 60 км/ч!"
                f"Ваша скорость - {self.speed} км/ч!")
        else:
            print('Скорость машины в норме!')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        print('Это рабочая машина!')
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости! Данная машина не может ехать со скоростью более 40 км/ч!"
                f"Ваша скорость - {self.speed} км/ч!")
        else:
            print('Скорость машины в норме!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        print('Это спортивная машина!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)
        print('Это полицейская машина!')


car_1 = WorkCar(70, 'white', 'Audi')
car_1.go()
car_1.show_speed()
car_1.turn('лево')
car_1.stop()
print(car_1.name)

car_2 = TownCar(30, 'black', 'BMW')
car_2.show_speed()
print(car_2.is_police)

car_3 = SportCar(100, 'yellow', 'Mazda')
car_3.show_speed()
print(car_3.color)

car_4 = PoliceCar(80, 'white+blue', 'Maserati', True)
car_4.go()
print(car_4.is_police)
