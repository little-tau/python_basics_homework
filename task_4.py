from abc import ABC, abstractmethod
import json


class Warehouse:
    def __init__(self):
        self.inv_seq = 0
        self.db = []
        self.departments = ["it", "secretary", "lawyers", "sales", "warehouse"]

    @classmethod
    def deserialize_db(cls):
        # Create Warehouse object from file.
        try:
            with open("task_4.txt", mode='r', encoding='utf-8') as db_file:
                db = json.load(db_file)
                for i in db['db']:
                    i['equipment'] = OfficeEquipment.deserialize_equipment(i['equipment'])
            wh = cls()
            wh.__dict__ = db
            return wh
        except FileNotFoundError:
            print("Cannot open database")
            wh = cls()
            return wh

    def serialize_db(self):
        # Save our work to file.
        with open("task_4.txt", mode='w', encoding='utf-8') as db_file:
            db = self.db
            for i in db:
                i['equipment'] = i['equipment'].__dict__
            di = self.__dict__
            di['db'] = db
            json.dump(di, db_file, indent=4, ensure_ascii=False)

    def show_departments(self):
        print(f"{self.departments}")

    def add_equipment(self, itm):
        record = {'inventory_num': self.new_inventory_num(itm), 'equipment': itm, 'price': itm.price,
                  'department': 'warehouse'}
        self.db.append(record)

    def remove_equipment(self, inv_num):
        for i in self.db:
            if i['inventory_num'] == inv_num:
                self.db.remove(i)
                print(f"The {i['equipment']} was removed")

    def show_dept_equipment(self, dept):
        if not self.check_department(dept):
            print(f"The department {dept} does not exist")
            return False
        for i in self.db:
            if i['department'] == dept:
                for k in i.keys():
                    print(f"{i[k]}", end=" ")
                print("\n", end="")
        return True

    def show_all_equipment(self):
        for i in self.db:
            for k in i.keys():
                print(f"{i[k]}", end=" ")
            print("\n", end="")

    def transfer_equipment(self, inv_num, dept):
        # Move the equipment to another department.
        if not self.check_department(dept):
            print(f"The department {dept} does not exist")
            return False
        else:
            for i in self.db:
                if i['inventory_num'] == inv_num:
                    i['department'] = dept
                    print(f"The {i['equipment']} was transferred to {i['department']}")
            return True

    def new_inventory_num(self, itm):
        # The unique sequence of inventory numbers.
        self.inv_seq += 1
        return f"{itm.inv_prefix}{self.inv_seq}"

    def check_department(self, dept):
        # Check if the department exists.
        if dept not in self.departments:
            return False
        else:
            return True


class OfficeEquipment(ABC):
    def __init__(self, manufacturer, model, serial_num, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.serial_num = serial_num
        self.name = 'noname'

    def __str__(self):
        return f"{self.name}({self.manufacturer} {self.model}) SN-{self.serial_num}"

    @abstractmethod
    def inv_prefix(self):
        # Unique inventory prefix.
        pass

    @classmethod
    def create_equipment(cls):
        # Create object from user input.
        manufacturer = input("Enter manufacturer: ")
        model = input("Enter model: ")
        serial_num = input("Enter serial number: ")
        try:
            price = abs(float(input("Enter price: ")))
        except ValueError:
            print("Incorrect value for price.")
            return False
        else:
            return cls(manufacturer, model, serial_num, price)

    @staticmethod
    def deserialize_equipment(d):
        # The deserialization is dependant of each subclass's constructor.
        # For the simplicity I would pop the redundant attributes.
        if d['name'] == 'printer':
            d.pop('name', None)
            return Printer(**d)
        if d['name'] == 'scanner':
            d.pop('name', None)
            return Scanner(**d)
        if d['name'] == 'copier':
            d.pop('name', None)
            return Copier(**d)


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, serial_num, price):
        super().__init__(manufacturer, model, serial_num, price)
        self.name = 'printer'

    @property
    def inv_prefix(self):
        return 'PNR'


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, serial_num, price):
        super().__init__(manufacturer, model, serial_num, price)
        self.name = 'scanner'

    @property
    def inv_prefix(self):
        return 'SCN'


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, serial_num, price):
        super().__init__(manufacturer, model, serial_num, price)
        self.name = 'copier'

    @property
    def inv_prefix(self):
        return 'CPR'


def print_help():
    print(
        f"* - exit, \np - add printer, \ns - add scanner, \nc - add copier, \nl - show warehouse, "
        f"\nt - transfer item, \nr - remove item, \nd - show departments")


# w = Warehouse()
# w.add_equipment(Printer('Xerox', 'Phaser 3020', 'SN764376', 200))
# w.add_equipment(Printer('Xerox', 'Phaser 6020', 'SN764376', 300))
# w.add_equipment(Scanner('HP', 'ScanJet Pro N4000', 'SN654GFD', 500))
# w.add_equipment(Copier('HP', 'ENVY Photo 7855', 'SNASJ76D', 900))
# w.serialize_db()

w = Warehouse.deserialize_db()

print_help()
while True:
    cmd = input("Next command: ")
    if cmd == '*':
        print(f"Ok, bye-bye")
        break
    if cmd == "p":
        a = Printer.create_equipment()
        if a:
            w.add_equipment(a)
    if cmd == "s":
        a = Scanner.create_equipment()
        if a:
            w.add_equipment(a)
    if cmd == "c":
        a = Copier.create_equipment()
        if a:
            w.add_equipment(a)
    if cmd == "l":
        dept = input("Which department? ")
        if not dept:
            w.show_all_equipment()
        else:
            w.show_dept_equipment(dept)
    if cmd == "t":
        num = input("What inventory number? ")
        dept = input("To which department? ")
        w.transfer_equipment(num, dept)
    if cmd == "r":
        num = input("What inventory number? ")
        w.remove_equipment(num)
    if cmd == "h":
        print_help()
    if cmd == "d":
        w.show_departments()
    else:
        pass

w.serialize_db()
