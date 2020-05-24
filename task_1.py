# The class instance must be created via fabric method only!

from re import search


class Date:
    def __init__(self, date):
        self.day, self.month, self.year = map(int, date.split('-'))

    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

    def decode_month(self):
        months_dict = {1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN", 7: "JUL", 8: "AUG", 9: "SEP",
                       10: "OCT", 11: "NOV", 12: "DEC"}
        return f"{self.day}-{months_dict[self.month]}-{self.year}"

    @classmethod
    def create_date(cls, date):
        match = search(r'\d{2}-\d{2}-\d{4}', date)
        if match:
            day, month, year = map(int, match.group().split('-'))
        else:
            raise ValueError("No date pattern found")
        is_valid, msg = cls.validate_date(day, month, year)
        if is_valid:
            return cls(match.group())
        else:
            raise ValueError(msg)

    @staticmethod
    def validate_date(day, month, year):
        # Making explicit if-branches for the readability.
        if not 1 <= year <= 3000:
            return False, "Year out of range"
        if month not in range(1, 13):
            return False, "Month out of range"
        if month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return False, "Leap year error"
        if day == 31 and month not in [1, 3, 5, 7, 8, 10, 12]:
            return False, "Month has < 31 days"
        if day > 29 and month == 2:
            return False, "February has 28 or 29 days"
        else:
            return True, "Valid date"


# Check staticmethod
print(Date.validate_date(31, 8, 2020))

# Check invalid date
try:
    d = Date.create_date('31-06-2020')
except ValueError as e:
    print(e)
else:
    print(d)
    print(d.decode_month())

# Check date created via fabric method
try:
    d = Date.create_date('31-08-2020')
except ValueError as e:
    print(e)
else:
    print(d)
    print(d.decode_month())
