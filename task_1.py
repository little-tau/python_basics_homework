from time import sleep
from itertools import cycle


class TrafficLight:
    colors = {"red": 7, "yellow": 3, "green": 5}
    style = {"red": '1;30;41m', "yellow": '1;30;43m', "green": '1;30;42m'}

    def __init__(self, color):
        self.__color = color
        self.__new_color = self.__position_color()
        print(f"The traffic light is loading at: \x1b[{TrafficLight.style[self.__color]}{self.__color}\x1b[0m")

    def __position_color(self):
        gen = cycle(TrafficLight.colors.keys())
        while next(gen) != self.__color:
            pass
        return gen

    def __cycle_colors(self):
        yield TrafficLight.colors[self.__color]

    def __switch_color(self):
        self.__color = next(self.__new_color)
        return self.__color

    def running(self):
        sleep_time = TrafficLight.colors[self.__color]
        sleep_cnt = sleep_time
        for n in range(sleep_time):
            print(f"\r\x1b[{TrafficLight.style[self.__color]}{self.__color}\x1b[0m wait [ {sleep_cnt} ]", end="")
            sleep(1)
            sleep_cnt -= 1
        self.__switch_color()
        print(f"\r\r", end="")


t = TrafficLight('green')
for i in range(3):
    t.running()
