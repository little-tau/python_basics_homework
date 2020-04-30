achievement1 = int(input("Enter the 1st athlete's achievement: "))
achievement2 = int(input("Enter the 2nd athlete's achievement: "))
i = 1
achievement_tmp = achievement1
while achievement_tmp < achievement2:
    i = i + 1
    achievement_tmp += achievement_tmp / 10
    print(f"{achievement_tmp:.2f}km day {i}")
if achievement1 > achievement2:
    print(f"The athlete will achieve at least {achievement2:.2f}km at day {i}. Actually he will run {achievement1:.2f}km")
else:
    print(f"The athlete will achieve {achievement_tmp:.2f}km at day {i}")
