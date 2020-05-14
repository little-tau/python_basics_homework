import re as re

print(f"\nThe file:")
with open('task_6_file.txt', mode='r', encoding='utf-8') as the_file:
    for line in the_file:
        print(line.strip())

"""
Without re
"""
study_hours_1 = {}
with open('task_6_file.txt', mode='r', encoding='utf-8') as the_file:
    for line in the_file:
        name, hours = line.split(':', 1)
        hours_list = list(map(int, [a if a != '' else 0 for a in
                                    [''.join(list(filter(lambda ch: ch in '0123456789', x))) for x in hours.split()]]))
        study_hours_1[name] = sum(hours_list)

print(f"\nThe results 1:")
for i in study_hours_1.keys():
    print(f"{i}: {study_hours_1[i]}")

"""
With re
"""
study_hours_2 = {}
with open('task_6_file.txt', mode='r', encoding='utf-8') as the_file:
    for line in the_file:
        match = re.match(r"(.*):\s(\d+|-)(\(л\))?\s(\d+|-)(\(пр\))?\s(\d+|-)(\(лаб\))?", line.strip())
        if match:
            name = match.group(1)
            hour_list = [int(x.replace('-', '0')) for x in [match.group(2), match.group(4), match.group(6)]]
            study_hours_2[name] = sum(hour_list)

print(f"\nThe results 2:")
for i in study_hours_1.keys():
    print(f"{i}: {study_hours_1[i]}")