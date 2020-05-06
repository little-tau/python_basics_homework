def sum_or_exit(numbers, s_char="*"):
    """ Returns sum of digits. Exit when encounter special character. """
    res = 0
    for num in numbers:
        if num == s_char:
            return res, -1
        else:
            try:
                res += float(num)
            except ValueError:
                return 0, -2
    return res, 0


rr = 0
while True:
    digits = input("Enter the string of digits (* for exit): ").split()
    r, code = sum_or_exit(digits)
    if code == -1:
        print(f"The final result is: {r + rr}")
        break
    if code == -2:
        print(f"Incorrect values")
    else:
        rr += r
        print(f"The result is: {rr}")
