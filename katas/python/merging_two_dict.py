# merge two dictionaries

def merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {"a" : 10, "b" : 9}
dict2 = {"d" : 5, "c" : 3}

print(merge(dict1, dict2))
print(dict2)