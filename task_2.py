seconds = int(input("Enter seconds: "))
days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 3600 // 60
seconds_remain = seconds % 60
print(f"+{days} {hours:02d}:{minutes:02d}:{seconds_remain:02d}")