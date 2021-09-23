def numberOfSetBits(value):
    result = 0
    m = 1
    while(value):
        result += value & m # bitwise & with 0x1
        value = value >> 1 # shift right
    return result

v = 24
print(numberOfSetBits(v))