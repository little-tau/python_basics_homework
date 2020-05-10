# Salary accounting.

from sys import argv

if (len(argv) == 2 and argv[1] == "-h") or (len(argv) == 1):
    print("Help: arguments:\n work hours (h),\n wage rate ($/h),\n bonus pay (%)\n")
    exit(-1)
elif len(argv) > 4:
    print("Wrong number of arguments. Type -h for help.")
    exit(-2)
try:
    work_hours = int(argv[1])
    wage_rate = float(argv[2])
    bonus_pay = int(argv[3])
except ValueError:
    print("Wrong type of arguments. Type -h for help.")
    exit(-3)

if bonus_pay < 0:
    print(f"The bonus cannot be negative")
    exit(-4)

income_tax = 0.13
sal_before_tax = (work_hours * wage_rate) * (1 + bonus_pay / 100)
sal_after_tax = sal_before_tax * (1 - income_tax)
print(f"Salary before tax: {sal_before_tax:.2f} $")
print(f"Salary after tax: {sal_after_tax:.2f} $")

