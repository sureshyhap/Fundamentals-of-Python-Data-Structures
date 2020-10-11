def expo(num, power):
    if power == 0:
        return 1
    # Odd power
    if power % 2 == 1:
        return num * expo(num, power - 1)
    # Even power
    else:
        return expo(num, power / 2) * expo(num, power / 2)

print(expo(3, 3))
    
