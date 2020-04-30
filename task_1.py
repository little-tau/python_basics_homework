order = int(input("Enter the order for the Sierpinski triangle (default is 4, believe me, it's enough):") or 4)
caption = str(input("Enter the caption for the art (Sierpinski triangle):") or "Sierpinski triangle")

size = 1 << order
y = size - 1
print(f"{caption} \n")
while y >= 0:
    i = 0
    s = ''
    while i <= y:
        s = s + " "
        i = i + 1
        x = 0
    while x < size - y:
        if x & y != 0:
            s = s + "  "
        else:
            s = s + "* "
        x = x + 1
    y = y - 1
    print(s)
print("\n")
while True:
    answer = str(input("Do you like the painting? y/n "))
    if answer == "y":
        print("Ok, Good")
        break
    elif answer == "n":
        print("You are too demanding")
        break
    else:
        print("Think again")
