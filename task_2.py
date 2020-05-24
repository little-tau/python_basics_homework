class SingularityException(Exception):
    pass


print(f"Going to do a / b")
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if b == 0:
        raise SingularityException(f"Division by zero leads to Singularity!")
except SingularityException as e:
    print(e)
except ValueError as e:
    print(f"Value error! {e}")
else:
    print(f"a/b = {round(a / b, 4)}")

print("Next action")
