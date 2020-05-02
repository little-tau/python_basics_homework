# Split the string and trim large words to 10 chars.
# If sep is not specified or None, any whitespace string is a separator.
the_string_list = input("Input the string: ").split()
for idx, elem in enumerate(the_string_list):
    print(f"{idx:} {elem[:10:]}")
