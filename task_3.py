num = int(input("Enter number: "))
i = int(input("Enter iterations (default is 3): ") or 3)
k = ''
loop_num = 0
while i > 0:
    k = str(k)+str(num)
    loop_num = loop_num + int(k)
    print(f"new number={k} result={loop_num} loop={i}")
    i = i - 1
print(f"The final number is {loop_num }")