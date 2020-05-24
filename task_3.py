class MyListExceptWrongVal(Exception):
    pass


class MyListExceptEnd(Exception):
    pass


class MyList:
    def __init__(self):
        self.lst = []

    @classmethod
    def init_list(cls, lst):
        new_list = cls.__new__(cls)
        try:
            new_list.lst = list(map(float, lst))
        except ValueError:
            return cls()
        else:
            return new_list

    def append(self, el):
        if el == '*':
            raise MyListExceptEnd("Exception! End of list.")
        try:
            float(el)
        except ValueError:
            raise MyListExceptWrongVal("Exception! Not a number.")
        else:
            self.lst.append(float(el))

    def __str__(self):
        return f"{self.lst}"


the_list = MyList.init_list([1, 2, 3, 9.8])
print(f"The original list: {the_list}")
while True:
    digit = input("Enter the digit (* for exit): ")
    try:
        the_list.append(digit)
    except MyListExceptEnd as e:
        print(e)
        break
    except MyListExceptWrongVal as e:
        print(e)
print(f"The resulting list is {the_list}")
