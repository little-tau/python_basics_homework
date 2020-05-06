def exp_simple(b=24.7, e=3):
    """ Simple exponentiation
        return -> b ^ e
    """
    return 1 / (b ** abs(e)) if e < 0 else b ** e


def exp_binary(b=24.7, e=3):
    """ Left to right binary exponentiation
        return -> b ^ e
    """
    binary_exp = list(reversed(bin(abs(e))[2:]))
    r = 1
    p = b
    for bit in binary_exp:
        if bit == '1':
            r *= p
        p *= p
    return 1 / r if e < 0 else r


print(f"Sample output:\n"\
      f"Binary exp: 24.7 ^ 3 = {exp_binary():.3f}\n"\
      f"Simple exp: 24.7 ^ 3 = {exp_simple():.3f}\n")
func_arr = [exp_simple, exp_binary]
base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

for f in func_arr:
    print(f"{base} ^ {exp} = {f(base, exp):.10f}")
