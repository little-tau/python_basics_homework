from random import randint

num_str = " ".join([str(randint(1, 1000)) for _ in range(100000)])
with open('task_5_file.txt',  mode='w+', encoding='utf-8') as the_file:
    the_file.write(num_str)
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))


