def division(value):
    try:
        x = 5/value  # this might generate an div0 error
        print(x)
    except ZeroDivisionError:
        print("Hey! You cannot divide by zero")


division(0)
print("So I keep going!")
