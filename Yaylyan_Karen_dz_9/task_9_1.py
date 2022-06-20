from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        while True:
            print(f'цвет светофора: ', self.__color)
            sleep(7)

            self.__color = 'жёлтый'
            print(f'цвет светофора: ', self.__color)
            sleep(2)

            self.__color = 'зелёный'
            print(f'цвет светофора: ', self.__color)
            sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
