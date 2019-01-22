#!/usr/bin/env python3

# conditionals blocks work by Indentation

x = 60
y = 42

print(f'x = {x}')
print(f'y = {y}')
print('Is x > y?')

if x > y:  # statement
    print(f'Yes, {x} is greater, than {y}.')  # if statement TRUE
elif x < y:
    print(f'No! {x} is NOT greater than {y}.')
else:
    print(f'Yes! {x} is equal to {y}.')

# inline conditional
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# operators
# ==
# !=
# > <
# <= >=
# logical operators and or not
# identity operators x is y , x is not y
# membership operator, x in y , x not in y
