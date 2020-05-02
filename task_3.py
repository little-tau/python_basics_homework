# Find the month to season mapping
# List the seasons
seasons = ['winter', 'spring', 'summer', 'autumn']
seasons_mapping = {}
# Fill mapping for each month. Don't want to fill the dict manually.
for i in range(1, 13):
    seasons_mapping[i] = seasons[((i % 12 + 3) // 3) - 1]

print(f"The full list of seasons is {seasons_mapping}")

mon = int(input("Enter the month's number 1..12: "))
if 13 > mon > 0:
    print(f"The season for the {mon} month is {seasons_mapping.get(mon)} via dict")
    print(f"The season for the {mon} month is {seasons[((mon % 12 + 3) // 3) - 1]} via list")
else:
    print(f"Illegal month number")
