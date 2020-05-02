# Swap elements in list.
the_list = []
list_card = int(input("How many elements in list? (5 is default): ") or 5)
print(f"Now input {list_card} elements of the list")
for i in range(0, list_card):
    list_element = input()
    the_list.append(list_element)

print(f"The original list is: {the_list}")

i = 0
while i <= len(the_list) // 2:
    the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
    i += 2

print(f"The swapped list is: {the_list}")
