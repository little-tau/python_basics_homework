the_file = open('task_1_file.txt', mode='w', encoding='utf-8')

while True:
    line = input("Enter line: ")
    if not line:
        break
    else:
        the_file.write(line+'\n')
the_file.close()
