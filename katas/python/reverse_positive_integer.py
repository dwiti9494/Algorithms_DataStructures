# reverse the positive integer 123456789

def reverse_int(n):
    x = 0
    while n > 0:
        x *= 10
        x += n % 10
        n //= 10 # / == normal divide == 123/10 = 12.3, floor divide == 123//10 = 12
    return x
print (reverse_int(123456789))