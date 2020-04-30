num = int(input("Enter number: "))
max_num = num % 10
res = 0
while num > 0:
    num = num // 10
    res = num % 10
    if max_num == 9:
        break
    elif max_num < res:
        max_num = res
    print(f"num={max_num} num={num}")
print(f"The max number = {max_num}")
