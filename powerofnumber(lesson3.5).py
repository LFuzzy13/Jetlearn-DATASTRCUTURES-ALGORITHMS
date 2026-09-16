def power(number, exponent):

    if exponent == 0:
        return 1

    return number * power(number, exponent - 1)


print(power(6,4))