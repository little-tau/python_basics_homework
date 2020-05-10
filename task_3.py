# Find numbers multiple of 20 or 21 in range of 20..240
from itertools import count

# Solution in one line
list_20_21 = [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]
print(f" The multiples of 20 and 21 are: {list_20_21}")


# Solution with custom generator
def gen_count(n, a, b):
    k = (a // n) + int(bool(a % n))
    for i in count(k):
        if a <= i * n <= b:
            yield i * n
        else:
            break


list_20_21_1 = [x for y in map(lambda y: list(gen_count(y, 20, 240)), [21, 20]) for x in y]
print(f" The multiples of 20 and 21 are: {sorted(list_20_21_1)}")
