my_file = open("sample_text.txt", "at")
# w - creates but if exists overwrites
# a - creates if not exist. if exists appends
# r - readmode, do not mess anything
print("me llamo fran", file=my_file)
my_file.close()  # is a good practice
print("done")
