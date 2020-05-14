import json

company_info = []
company_avg = {}
company_profit = {}
company_loses = {}
avg_profit = {"average_profit": 0}

i = 0
p = 0
print(f"All companies:\n")
with open('task_7_file.txt', mode='r', encoding='utf-8') as the_file:
    for line in the_file:
        revenue, expenses = list(map(float, line.split()[-2:]))
        company = " ".join(line.split()[:-3])
        profit = round((revenue - expenses), 2)
        if profit <= 0:
            company_loses[company] = profit
        else:
            company_profit[company] = profit
            i += 1
            p += profit
            avg_profit["average_profit"] = round(p / i, 2)
        company_avg[company] = profit
        print(f"{company} {revenue} {expenses}")

company_info.append(company_avg)
company_info.append(avg_profit)
print(f"\nCompanies with profit: {company_profit}")
print(f"Companies without profit: {company_loses}")
print(f"All companies: {company_avg}")
print(f"Average profit: {avg_profit}")


with open('task_7_json.json', mode='w', encoding='utf-8') as the_file:
    json.dump(company_info, the_file, indent=4, ensure_ascii=False)


with open('task_7_json.json', mode='r', encoding='utf-8') as the_file:
    info = json.load(the_file)
    print(f"All info:\n{json.dumps(info, indent=4, ensure_ascii=False)}")


