# Output different types
type_list = ["string type", 0.6, 88, True, ["one", "two"], (1, 2), complex(8, -1), None, float("inf")]
for i in type_list:
    print(f"type: {type(i)} value: {i}")
