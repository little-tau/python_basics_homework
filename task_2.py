class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, height=5, unit_mass=25):
        # height - cm
        # unit mass kg/cm
        return round(self._length * self._width * height * unit_mass / 1000, 2)


# 20м * 5000м * 25кг * 5см = 12500 т

r = Road(5000, 20)
print(f"The mass of asphalt is: {r.get_mass(5, 25)} ton")
