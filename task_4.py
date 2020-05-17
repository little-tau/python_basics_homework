# Simple car movement.
# Car can accelerate only in x direction.
# Car can move to the specific direction only with constant speed.
# Car collisions are not considered.

from math import sqrt


class Physics:
    def __init__(self, x, y):
        # _a - acceleration
        # _x, _y - coordinates
        # _v - velocity
        # _t - time elapsed
        # _max_speed - the maximum speed of the vehicle.
        self._x = x
        self._y = y
        self._v = 0
        self._a = 0
        self._t = 0
        self._max_speed = 0

    def accelerate_to_v(self, v):
        # time - seconds
        # acceleration - km/h*s
        # velocity - km/h
        if v >= self._max_speed:
            v = self._max_speed
        elif v < 0:
            v = 0
        if not self._is_started:
            return self._x, self._y, 0
        t = abs(round((v - self._v) / self._a, 2))
        s = abs(round((pow(v, 2) - pow(self._v, 2)) / (7200 * self._a), 2))
        self._v = v
        self._t = round(self._t + t, 2)
        self._x = round(self._x + s, 2)
        return self._x, self._y, t

    def move_by_xy(self, x, y):
        # move by (x, y) forward
        # x, y - km
        # time - seconds
        if not self._is_started or self._v == 0:
            return self._x, self._y, 0
        t = round(sqrt(pow(x, 2) + pow(y, 2)) * 3600 / self._v, 2)
        self._x = round(self._x + x, 2)
        self._y = round(self._y + y, 2)
        self._t = round(self._t + t, 2)
        return self._x, self._y, t

    def move_to_xy(self, x, y):
        # move to (x, y) coordinate
        # x, y - km
        # time - seconds
        if not self._is_started or self._v == 0:
            return self._x, self._y, 0
        x1 = x - self._x
        y1 = y - self._y
        t = round(sqrt(pow(x1, 2) + pow(y1, 2)) * 3600 / self._v, 2)
        self._x = round(x, 2)
        self._y = round(y, 2)
        self._t = round(self._t + t, 2)
        return self._x, self._y, t

    def get_xy(self):
        return self._x, self._y

    def get_total_time(self):
        return self._t


class Car(Physics):
    def __init__(self, color, name, x, y):
        super().__init__(x, y)
        self.color = color
        self.name = name
        self._is_police = False
        self._is_started = False

    def get_police(self):
        return self._is_police

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def show_speed(self):
        return self._v, "Allowed"

    def get_overall_info(self):
        return f"{self.get_name()}: New pos: ({self._x}, {self._y}). Speed: {self.show_speed()}. Elapsed: {self._t}"

    def stop(self):
        if self._is_started:
            x, y, t = self.accelerate_to_v(0)
            self._is_started = False
            return f"Stopped {self.name}. New position ({x}, {y}). Time to stop: {t} seconds"
        else:
            return "Already stopped"

    def start(self, v):
        if not self._is_started:
            self._is_started = True
            x, y, t = self.accelerate_to_v(v)
            return f"Started {str(self.name)}. New position ({x}, {y}). Time to start: {t} seconds"
        else:
            return "Already started"


class TownCar(Car):
    def __init__(self, color, name, x, y):
        super().__init__(color, name, x, y)
        self._a = 25
        self._max_speed = 150
        self._speed_allowed = 60
        self._is_police = False

    def show_speed(self):
        return (self._v, "Allowed") if self._v < self._speed_allowed else (self._v, "Not allowed")


class WorkCar(Car):
    def __init__(self, color, name, x, y):
        super().__init__(color, name, x, y)
        self._a = 2
        self._max_speed = 50
        self._speed_allowed = 40
        self._is_police = False

    def show_speed(self):
        return (self._v, "Allowed") if self._v < self._speed_allowed else (self._v, "Not allowed")


class SportCar(Car):
    def __init__(self, color, name, x, y):
        super().__init__(color, name, x, y)
        self._a = 55
        self._max_speed = 300
        self._speed_allowed = 150
        self._is_police = False

    def show_speed(self):
        return (self._v, "Allowed") if self._v < self._speed_allowed else (self._v, "Not allowed")


class PoliceCar(Car):
    def __init__(self, color, name, x, y):
        super().__init__(color, name, x, y)
        self._a = 30
        self._max_speed = 250
        self._is_police = True

    def show_speed(self):
        return self._v, "Allowed"


car_1 = PoliceCar('White', 'Toyota', 0, 0)
car_2 = SportCar('White', 'Delorean', 0, 0)
car_3 = TownCar('Silver', 'Tesla', 0, 0)
car_4 = WorkCar('Yellow', 'Komatsu', 0, 0)

cars = [car_1, car_2, car_3, car_4]
analytics = {}
for i in cars:
    print(f"\nCar {i.get_name()} speed {i.show_speed()}. Is police: {i.get_police()}")
    print(i.start(97))
    nx, ny, tn = i.accelerate_to_v(150)
    print(f"{i.get_overall_info()} Time to move {tn}")
    nx, ny, tn = i.move_by_xy(10, 2)
    print(f"{i.get_overall_info()} Time to move {tn}")
    nx, ny, tn = i.move_to_xy(12, 2)
    print(f"{i.get_overall_info()} Time to move {tn}")
    nx, ny, tn = i.accelerate_to_v(100)
    print(f"{i.get_overall_info()} Time to move {tn}")
    print(i.stop())
    print(f"Total time: {i.get_total_time()} seconds")
    analytics[i.get_name()] = i.get_total_time()

print(f"\nAnalytics:")
for i in analytics.keys():
    print(f"{i} took {analytics[i]} seconds to move")


