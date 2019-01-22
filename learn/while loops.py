#!/usr/bin/env python3

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
n = 0

while (n < 7):  # print the 7 first days of the list
    print(days[n])
    n += 1

# fibonacci series
# end parameter prints a space after b
# flush
a, b = 0, 1
while (b < 10):
    print(b, end=' ', flush=True)
    # end =' ' prints a space rather than a new line
    a, b = b, a+b
print()  # line ending

# continue, break and else controls
password = "hola"
login = ""
auth = False
count = 0
max_attempts = 3

while login != password:
    count += 1
    if count > max_attempts:
        break
    login = input(f"Attempt {count}/{max_attempts}. What is the password? ")
else:
    auth = True
print("Authorized" if auth else "Calling the FBI...")
