"""
Create file with test data
"""
# people = [
#     "Jeff Bezos 143000.4",
#     "Bill Gates 106000.3",
#     "Bernard Arnault 92000.7",
#     "Mark Zuckerberg 78000.3",
#     "Warren Buffett 69000.8",
#     "Larry Ellison 67000.4",
#     "Steve Ballmer 65000.8",
#     "Larry Page 62000.6",
#     "Sergey Brin 60000.3",
#     "Amancio Ortega 60000.1",
#     "Michael Bloomberg 58000.0",
#     "Mukesh Ambani 56000.8",
#     "Francoise Bettencourt Meyers 54000.9",
#     "Jim Walton 54000.7",
#     "Alice Walton 54000.5",
#     "Rob Walton 54000.3",
#     "Carlos Slim Helu 51000.1",
#     "Klaus-Michael Kuehne 20000.0",
#     "Joseph Safra 19000.8",
#     "Susanne Klatten 19000.4",
#     "Qin Yinglin 19000.2",
#     "Laurene Powell Jobs 19000.1",
#     "Vagit Alekperov 18000.9",
#     "Lukas Walton 18000.7",
#     "Len Blavatnik 18000.5",
#     "Alexey Mordashov 18000.5"
# ]
#
# with open('task_3_file.txt',  mode='w', encoding='utf-8') as the_file:
#     the_file.write("\n".join(people))


i = 0
total_money = 0
print(f"People with less than 20000.0 abstract coins:\n")
try:
    with open('task_3_file.txt', mode='r', encoding='utf-8') as the_file:
        for line in the_file:
            try:
                money = float(line.split()[-1])
            except ValueError:
                print("Wrong data")
                exit(-1)
            if money < 20000:
                print(line, end="")
            i += 1
            total_money += money
    print(f"\n\nThe number of people: {i}")
    print(f"Average abstract coins: {total_money / i:.2f}")
except FileNotFoundError:
    print("No such file or directory")


