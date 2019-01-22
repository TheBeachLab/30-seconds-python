my_string = "Hello, how are you?"

my_long_string = """
Hi,

My name is Fran.

Blah, blah, blah.
"""

# length of a string
print(len(my_string))

# get a specific character, 0 is first one
print(my_string[0])

# negative values start from the end
print(my_string[-2])

# access a specific range of characters
print(my_string[0:3])  # 3 characters, start at 0 index
print(my_string[:3])

print(my_string[0:])  # these get all the string
print(my_string[:])

# escape character \ to include a special character in python
# \"
# \'
# \\
# |n  this is a new line

print("Hi,\nHello")

# concatenation
first = "Fran"
last = "Sanchez"
full = f"{first} {last}, 2 = 2 equals {2+2}.\nMy name has {len(first)} letters."
print(full)

# split
text = "Hola, me llamo Fran. Como estas?"
list = text.split()  # this creates a list of splitted by default space
print(list)
new_text = ":".join(list)  # rejoins the text with : as separator
print(new_text)
