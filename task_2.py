from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def show_fabric_consumption(self):
        pass


class Coat(Clothes):
    sizes = [38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

    def __init__(self, v, n=1):
        self.v = v
        self.n = n
        self.name = 'coat'

    def show_fabric_consumption(self):
        return round((self.v / 6.5 + 0.5) * self.n, 4)

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        self.__v = min(Coat.sizes, key=lambda x: abs(x - v))


class Costume(Clothes):
    heights = [146, 152, 158, 164, 170, 176]

    def __init__(self, h, n=1):
        self.h = h
        self.n = n
        self.name = 'costume'

    def show_fabric_consumption(self):
        return round((self.h * 2 + 0.3) * self.n, 4)

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = min(Costume.heights, key=lambda x: abs(x - h))


class Fabric:
    def __init__(self):
        self.costumes = []
        self.coats = []

    def __del__(self):
        print(f"The fabric object cleanup")

    def add_costume(self, c, n=1):
        self.costumes.append(Costume(c, n))

    def add_coat(self, c, n=1):
        self.coats.append(Coat(c, n))

    def show_fabric_consumption_all(self, name='all'):
        if name == 'costume':
            return round(sum([x.show_fabric_consumption() for x in self.costumes]), 4)
        elif name == 'coat':
            return round(sum([x.show_fabric_consumption() for x in self.coats]), 4)
        else:
            return round(sum([x.show_fabric_consumption() for x in self.coats]) + sum(
                [x.show_fabric_consumption() for x in self.costumes]), 4)

    def print_overall_info(self):
        print(f"The current material consumption is:")
        print(f"Coats: {self.show_fabric_consumption_all('coat')}")
        print(f"Costumes: {self.show_fabric_consumption_all('costume')}")
        print(f"Everything: {self.show_fabric_consumption_all()}\n")


f = Fabric()
f.add_coat(38)
f.print_overall_info()
f.add_coat(38, 6)
f.print_overall_info()
f.add_costume(152)
f.print_overall_info()
f.add_costume(152, 7)
f.print_overall_info()
del f

