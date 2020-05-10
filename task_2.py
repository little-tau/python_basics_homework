# Resulting list includes the numbers that are > than previous.
# add "if len(the_list) > 1 else the_list" to consider lists of 1 element.
# e.g the_reduced_list = [x for x, y in zip(the_list[1:], the_list[:-1]) if x > y] if len(the_list) > 1 else the_list
# [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# [12, 44, 4, 10, 78, 123]


def reduce_list_1(input_list):
    try:
        the_list = list(map(int, input_list))
        the_reduced_list = [x for x, y in zip(the_list[1:], the_list[:-1]) if x > y]
        return the_reduced_list
    except ValueError:
        return "ERROR - wrong data"


def reduce_list_2(input_list):
    try:
        the_list = list(map(int, input_list))
        the_reduced_list = [x for n, x in enumerate(the_list) if x > the_list[n - 1] and n > 0]
        return the_reduced_list
    except ValueError:
        return "ERROR - wrong data"


test_lists = [[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55],
              [9],
              [77, 9],
              [8, 99],
              [0, 'j', 'k', 8],
              [0, 0, 0],
              [1, 2, 3, 4, 5],
              [5, 4, 3, 2, 1],
              [5, 5, 5, 5, 5]]

for i in test_lists:
    print(f"Original list: {i} Reduced list 1: {reduce_list_1(i)}")
    print(f"Original list: {i} Reduced list 2: {reduce_list_2(i)}")
