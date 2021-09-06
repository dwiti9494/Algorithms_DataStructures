# Merging dict

dict_1 = {"a" : 1, "b" : 2}
dict_2 = {"b" : 3, "c" : 4, "d" : 6}
# merged = {**dict_1, **dict_2}
merged = dict_1 | dict_2
print(merged)