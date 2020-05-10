# [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# [23, 1, 3, 10, 4, 11]
from random import randint, shuffle


def throw_rand():
    """ Returns list with random elements containing some repeated elements """
    seed = list(set([randint(1, 1000) for _ in range(10)]))
    repeated = [x for y in [[randint(1, 100)] * randint(2, 5) for _ in range(3)] for x in y]
    # print(f"seed: {seed}")
    # print(f"repeated: {repeated}")
    repeated.extend(seed)
    shuffle(repeated)
    return repeated


# the_rand = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
the_rand = throw_rand()
the_result_list = [x for x in the_rand if the_rand.count(x) == 1]
print(f"The random sequence is: {the_rand}")
print(f"The resulting sequence is: {the_result_list}")
