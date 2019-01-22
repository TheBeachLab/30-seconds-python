# for loops
# using range
for number in range(5):
    print(number)


for number in range(3):  # number from 0 to 2
    print("Attempt ", number + 1, (number+1) * ".")


for number in range(1, 5):  # number from 1 to 4
    print("Attempt ", number, number * ".")


for number in range(1, 11, 2):  # number from 1 to 10 in 2 steps
    print("Attempt ", number, number * ".")

# nested loops
for x in range(3):
    for y in range(3):
        print(f"({x} , {y})")


# strings are also iterable
for x in "hello":
    print(x)


# lists are also iterable
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
for x in days:
    print(x)
