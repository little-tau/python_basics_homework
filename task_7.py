# The angles are in radian!

from math import cos, sin, sqrt, atan
import cmath


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(round(self.x * other.x - self.y * other.y, 2), round(self.x * other.y + self.y * other.x, 2))

    def __str__(self):
        return f"({self.x}+i{self.y})"

    @classmethod
    def new_complex_polar(cls, r, theta):
        x, y = cls.polar_to_cartesian(r, theta)
        return cls(x, y)

    @classmethod
    def new_complex_cartesian(cls, x, y):
        return cls(x, y)

    @staticmethod
    def polar_to_cartesian(r, theta):
        return round(r * cos(theta), 2), round(r * sin(theta), 2)

    @staticmethod
    def cartesian_to_polar(x, y):
        return round(sqrt(pow(x, 2) + pow(y, 2)), 2), round(atan(y / x), 2)


print(f"TESTING FUNCTIONS")
print(Complex.cartesian_to_polar(60, 70))
print(f"Check: {cmath.polar(60 + 70j)}")
print(Complex.polar_to_cartesian(92.2, 0.86))
print(f"Check: {cmath.rect(92.2, 0.86)}")

# Test sum and multiplication
z1 = complex(1, 9)
z2 = complex(6, 8)
print(f"TESTING OPERATIONS")
print(f"{z1} * {z2} = {z1 * z2}")
print(f"Check: {complex(1, 9) * complex(6, 8)}")
print(f"{z1} + {z2} = {z1 + z2}")
print(f"Check: {complex(1, 9) + complex(6, 8)}")

# Test fabric-initialized numbers
z3 = Complex.new_complex_polar(92.2, 0.86)
z4 = Complex.new_complex_cartesian(60, 70)
print(f"TESTING FABRIC METHODS")
print(f"{z3} * {z4} = {z3 * z4}")
print(f"Check: {cmath.rect(92.2, 0.86) * (60 + 70j)}")
print(f"{z3} + {z4} = {z3 + z4}")
print(f"Check: {cmath.rect(92.2, 0.86) + (60 + 70j)}")
