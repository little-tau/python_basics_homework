revenue = int(input("Enter your company revenue in $: "))
costs = int(input("Enter your company costs in $: "))
if revenue < costs:
    print(f"Warning! You're working with loss.")
else:
    return_on_revenue = (revenue - costs) * 100 / revenue
    print(f"Return on revenue is {return_on_revenue:.2f}%.")
    emp = int(input("Enter the number of employees: "))
    profit_per_emp = (revenue - costs) / emp
    print(f"The profit per employee is {profit_per_emp:.2f}$.")