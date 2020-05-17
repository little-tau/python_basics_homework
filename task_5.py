class Stationery:
    def __init(self, title):
        self.title = title

    def draw(self):
        print(f"Start drawing")


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f"This is a {self.title}. Start drawing")


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print(f"This is a {self.title}. Start drawing")


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f"This is a {self.title}. Start drawing")


class Apple(Stationery):
    def __init__(self):
        self.title = 'Apple'

    def draw(self):
        print(f"This is an {self.title}. Start drawing")


class Pineapple(Stationery):
    def __init__(self):
        self.title = 'Pineapple'

    def draw(self):
        print(f"Uuu, {self.title}. Start drawing")


a = Pen()
a.draw()
b = Apple()
b.draw()
c = Pineapple()
c.draw()
