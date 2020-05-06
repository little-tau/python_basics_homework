def sum_max_1(num1, num2, num3):
    """ Returns the sum of max two numbers(int/float). TypeError = e1"""
    try:
        a = sum(sorted([num1, num2, num3], reverse=True)[:2:])
    except TypeError:
        return 'e1'
    return a


def sum_max_2(num1, num2, num3):
    """ Returns the sum of max two numbers(int/float). TypeError = e1"""
    try:
        a = max(num1 + num2, num2 + num3, num1 + num3)
    except TypeError:
        return 'e1'
    return a


def sum_max_2_ext(*args, n=2):
    """
    Returns the sum of max n integers.
    Arguments:
           args -> integers
           n -> number of integers to sum. 2 is default.
    If n > len(args) then the sum(args) is returned
    """
    try:
        a = list(map(lambda x: int(x), sorted(args, reverse=True)[:int(n):]))
    except TypeError:
        return 'e1'
    except ValueError:
        return 'e2'
    return sum(a)


n1 = int(input('num1: '))
n2 = int(input('num2: '))
n3 = int(input('num3: '))
print(f"First method {sum_max_1(n1, n2, n3)}")
print(f"Second method {sum_max_1(n1, n2, n3)}")
print(f"Sample third method {sum_max_2_ext(0, 5, 5, 5, 3, 5, 0, -9, 9, n=6)}")
