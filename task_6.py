def int_func(word):
    """ Returns the word beginning from capital letter. """
    return str(word).title()


def is_lower_latin(word_list):
    """ True if the string is lowercase latin. False otherwise """
    flag = True
    for wrd in word_list:
        if sum(list(map(lambda x: 1 if ord(x) not in range(ord('a'), ord('z')) else 0, list(wrd)))) > 0:
            flag = False
            break
    return flag


while True:
    the_word_list = input("\nEnter your string: ").split()
    if not is_lower_latin(the_word_list):
        print(f"Illegal string. Should be lowercase latin.")
    else:
        break


print(f"The string is:", end=' ')
for w in the_word_list:
    print(f"{int_func(w)}", end=' ')

