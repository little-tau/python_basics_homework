from functools import reduce

n = reduce((lambda x, y: x * y), [n for n in range(100, 1001) if n % 2 == 0])

a = len(list(str(n))) - 1
print(f"The product of all even numbers 100..1000: {n}")
print(f"The short form is: {int(str(n)[:10]) / 10 ** 9} * 10^{a}")
