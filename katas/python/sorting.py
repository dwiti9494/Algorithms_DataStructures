# Sorting dict by values

# x = {1 : 2, 3 : 4, 4 : 3, 2 : 1, 0 : 0}
# x1 = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# print(x1)

# # Sorting a list
# x = [1, 2, 3, 5, 4, 7, 10, 21, 9]
# x.sort()
# print(x)

# Sorting a list of dictionaries by a value of dict

x = [
        {"name" : "Sam", "age" : 39},
        {"name" : "Ram", "age" : 42},
        {"name" : "Gam", "age" : 19},
    ]

newlist = sorted(x, key=lambda k: k["name"])
print(newlist)