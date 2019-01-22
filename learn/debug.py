def multiply_many(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


# insert a breakpoint F9 and run F5, then F10 or F11
print(multiply_many(2, 3, 4, 6))
