# Implement the goods structure
goods = []
default_goods = [{"name": "computer", "price": 20000, "count": 5, "unit": "item"},
                 {"name": "printer", "price": 6000, "count": 2, "unit": "item"},
                 {"name": "cola", "price": 10.5, "count": 209999, "unit": "litre"},
                 {"name": "energy", "price": 4988.9, "count": 876, "unit": "GeV"},
                 {"name": "scanner", "price": 2000, "count": 7, "unit": "item"},
                 {"name": "mouse", "price": 20.8, "count": 300, "unit": "item"},
                 {"name": "network", "price": 270.66, "count": 7, "unit": "Mib"}
                 ]
i = 1
while True:
    ans = input("Wanna to insert goods into table? (y/n) (or ENTER) ") or "y"
    if ans == "y":
        flag = 'NE'
        # We don't know regex yest, so there's no input validation.
        new_good = dict({"name": input("name: (or ENTER) ") or default_goods[(i - 1) % len(default_goods)].get("name"),
                         "price": input("price: (or ENTER) ") or default_goods[(i - 1) % len(default_goods)].get("price"),
                         "count": input("count: (or ENTER) ") or default_goods[(i - 1) % len(default_goods)].get("count"),
                         "unit": input("unit: (or ENTER) ") or default_goods[(i - 1) % len(default_goods)].get("unit")})
        print(f"Your good is {new_good}")
        for k in goods:
            if k[1]["name"] == new_good["name"]:
                print(f"The good already exists")
                flag = 'E'
                break
        if flag == 'NE':
            goods.append((i, new_good))
            i += 1
        else:
            continue
    elif ans == "n":
        break
    else:
        continue

# Print goods line by line
print("\nGoods:\n")
for v in goods:
    print(f"Good number {v[0]}")
    for k in v[1].keys():
        print(f"{k}: {v[1].get(k)}")
    print("\n")

# Compute analytics
goods_analytics = {"name": [], "price": [], "count": [], "unit": []}

# Fill the analytics dict
for element in goods:
    for k in element[1].keys():
        goods_analytics[k].append(element[1].get(k))
# Remove duplicate entries.
for k in goods_analytics.keys():
    goods_analytics[k] = list(set(goods_analytics.get(k)))

# Print analytics line by line
print("Goods analytics:\n")
for k, v in goods_analytics.items():
    print(f"{k}: {goods_analytics.get(k)}")

print(f"\nVerify goods structure {goods}")
print(f"Verify analytics structure {goods_analytics}")
