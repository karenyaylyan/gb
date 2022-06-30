class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости. Скоростное ограничение: 60')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости. Скоростное ограничение: 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


sport_car = SportCar(150, 'red', 'ferrari')
sport_car.go()
sport_car.turn('лево')
sport_car.stop()
sport_car.show_speed()

assert sport_car.speed == 150
assert sport_car.color == 'red'
assert sport_car.name == 'ferrari'
assert not sport_car.is_police

town_car = TownCar(65, 'white', 'toyota')
town_car.show_speed()

work_car = WorkCar(50, 'black', 'bmw')
work_car.show_speed()

police_car = PoliceCar(100, 'blue', 'mazda')
police_car.show_speed()

assert police_car.is_police
