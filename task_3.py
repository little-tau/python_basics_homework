class Cell:
    def __init__(self, subcells):
        self.subcells = subcells
        if self.subcells <= 0 or not isinstance(self.subcells, int):
            raise ValueError('Invalid cell!')

    def __add__(self, other):
        return Cell(self.subcells + other.subcells)

    def __sub__(self, other):
        return Cell(
            self.subcells - other.subcells) if self.subcells > other.subcells else "The first cell has no material " \
                                                                                   "for subtraction"

    def __truediv__(self, other):
        return self.subcells // other.subcells if self.subcells > other.subcells else "The first cell has no material" \
                                                                                     " for division"

    def __str__(self):
        return f"{self.subcells}"

    def make_order(self, n):
        cell_blueprint = ''
        for i in range((self.subcells // n)):
            cell_blueprint += f"{'*' * n}\n"
        cell_blueprint += f"{'+' * (self.subcells % n)}\n"
        return cell_blueprint


c1 = Cell(5)
c2 = Cell(28)
print(f"Cell {c1}")
print(f"Cell {c2}")
print(f"Cell division {c1} / {c2}: {c1 / c2}")
print(f"Cell division {c2} / {c1}: {c2 / c1}")
print(f"Cell sum {c1} + {c2}: {c2 + c1}")
print(f"Cell sub {c1} - {c2}: {c1 - c2}")
print(f"Cell sub {c2} - {c1}: {c2 - c1}")
print(c2.make_order(5))
