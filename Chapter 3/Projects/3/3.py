"""Exponent function.
   O(N)."""

def expo(num, power):
    i = 1;
    while i < power:
        num *= num
        i += 1
    return num

print(expo(5, 3))
