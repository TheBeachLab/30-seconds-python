high_income = True
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# or
# not
if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
