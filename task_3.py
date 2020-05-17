class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return round(self._income.get("wage") + self._income.get("bonus"), 4)


workers = [
    {"name": "Jeff", "surname": "Bezos", "position": "Amazon Boss", "wage": 143000.4, "bonus": 555.09},
    {"name": "Bill", "surname": "Gates", "position": "MS Boss", "wage": 106000.3, "bonus": 556.09},
    {"name": "Mark", "surname": "Zuckerberg", "position": "Facebook Boss", "wage": 78000.3, "bonus": 557.09},
    {"name": "Larry", "surname": "Ellison", "position": "Oracle Boss", "wage": 67000.4, "bonus": 559.09}
]

the_worker = []
j = 0
for i in workers:
    the_worker.append(Position(i.get("name"), i.get("surname"), i.get("position"), i.get("wage"), i.get("bonus")))
    print(f"The {the_worker[j].get_full_name()}'s total income is {the_worker[j].get_total_income()}")
    j += 1

