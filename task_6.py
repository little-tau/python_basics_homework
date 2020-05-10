from itertools import count, cycle, takewhile


def g_count(start, card):
    a = 0
    for i in count(start):
        yield i
        a += 1
        if a >= card:
            break


def g_cycle(lst, card):
    a = 0
    for i in cycle(lst):
        yield i
        a += 1
        if a >= card:
            break


# count iterator
gen_count = count(3)
gen_count_1 = g_count(3, 8)
iter_count = list(next(gen_count) for _ in range(3, 11))

# cycle iterator
list_cycle = [chr(x) for x in range(ord('A'), ord('C') + 1)]
gen_cycle = cycle(list_cycle)
gen_cycle_1 = g_cycle(list_cycle, 16)
iter_cycle = list(next(gen_cycle) for _ in range(16))

print(f"Count generator produced method 1: {iter_count}")
print(f"Count generator produced method 2: {list(gen_count_1)}")
print(f"Cycle generator produced method 1: {iter_cycle}")
print(f"Cycle generator produced method 2: {list(gen_cycle_1)}")

# restrict infinite generators with itertools function
gen_count = count(3)
gen_cycle = cycle(list_cycle)
print(f"Restricted count: {list(takewhile(lambda x: x < 11, gen_count))}")
print(f"Restricted cycle: {[e for i, e in takewhile(lambda x: x[0] < 16, enumerate(gen_cycle))]}")
