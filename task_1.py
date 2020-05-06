def divide_numbers(num, den):
    """
    Returns the ratio of two digits. Returns inf if we divide by zero.
    Arguments:
    num - numerator
    den - denominator
    """
    try:
        a = num / den
    except ZeroDivisionError:
        return float("inf")
    return a


n = float(input("Input numerator: "))
d = float(input("Input denominator: "))

print(f"{n}/{d} = {divide_numbers(n, d):.4f}")