a1 =[1, 3, 2, 3, 4, 3, 6, 3]
seen = set()
rep = set()
d = {}

# distributing them with key and value pair
for a in a1:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
print(d)

# find repetated number
for x in a1:
    if x in seen:
        rep.add(x)
    else:
        seen.add(x)
print(rep)