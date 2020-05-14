numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

line_numbers = []
try:
    with open('task_4_in.txt',  mode='r', encoding='utf-8') as in_file:
        for line in in_file:
            nam, num = line.strip().split(' - ')
            line_numbers.append(' - '.join([numbers[nam], num]))
except FileNotFoundError:
    print("No such file or directory")
    exit(-1)

with open('task_4_out.txt',  mode='w+', encoding='utf-8') as out_file:
    out_file.write("\n".join(line_numbers))
    out_file.seek(0)
    for line in out_file:
        print(line.strip())




