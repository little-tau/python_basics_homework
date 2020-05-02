# Implement the rating structure.
the_list = [7, 8, 3, 3, 2]
print(f"The original list is {the_list}")
# Make sure the list is reverse-sorted (using insertion sort). We can use sort method but we don't want to.
for i in range(0, len(the_list)):
    tmp_list = the_list[i]
    j = i
    while j > 0 and tmp_list > the_list[j - 1]:
        the_list[j] = the_list[j - 1]
        j -= 1
    the_list[j] = tmp_list

print(f"The pre-sorted list is {the_list}")

while True:
    val = input("Add the element to the rating (print e to exit): " or "e")
    if val == 'e':
        break
    elif val.lstrip("-").isdigit():  # consider negative integers.
        i = 0
        next_elem = int(val)
        for i in range(0, len(the_list)):
            if next_elem <= the_list[i]:
                i += 1
            else:
                break
        the_list.insert(i, next_elem)
        print(f" The position is {i} The list is {the_list}")
    else:
        continue
