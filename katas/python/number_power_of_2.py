def numberPowerOf2(value):
    return (value & (value - 1)) == 0

v = 16
w = 9
print(numberPowerOf2(v))
print(numberPowerOf2(w))