#•If the person is less than 2 years old, print a message that the person is a baby.
#•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#•If the person is age 65 or older, print a message that the person is an elder.

age=18
print("Age is 18")

if age<2:
    print("Baby")
elif age<4:
    print("Toddler")
elif age<13:
    print("Kid")
elif age<20:
    print("Teenager")
elif age<65:
    print("Adult")

else:
    print("Elder")