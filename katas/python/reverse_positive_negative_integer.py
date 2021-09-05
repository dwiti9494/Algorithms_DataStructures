# reverse the positive integer 12345
# reverse the negative integer -12345

def reverse_int(m):
    x = 0
    n = m
    if m < 0: # if m is negative
        n *= -1
    while n > 0: # if m is postive
        x *= 10
        x += n % 10
        n //= 10
    if m < 0:
        # concatenate a "-" sign at the end
        return "-" + str(x) 
    return x

print (reverse_int(12345))
print (reverse_int(-12345))