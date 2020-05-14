try:
    with open('task_2_file.txt', mode='r', encoding='utf-8') as the_file:
        i = 0
        for line in the_file:
            i += 1
            print(f"Line: {i}: {line.rstrip()}")
        i = 0
        the_file.seek(0)
        print("\n")
        for line in the_file:
            i += 1
            print(f"Line: {i}: Words: {len(line.rstrip().split())}")
    print(f"\nTotal lines in a file: {i}")
except FileNotFoundError:
    print("No such file or directory")
