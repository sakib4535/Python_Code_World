day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 or not raining:
    print("Go Outside and Walk Freely")
else:
    print("Stay at Home and Learn Python")

# Another One

day_1 = "Friday"
time_1 = 5
print(time_1)

day = "Sunday"
temp = 27
raining = True

if (day == "Saturday" and temp > 25) or not raining:     #This statement will show False# (False+ True = True(AND Gate)+ False = False(or gate);), and then move for the 'Else'
    print("Go For Walk")
else:
    print("learn Python")

# Another method

if 0:
    print("True")
else:
    print("False")

name = input("Please Enter Your Name Here: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Don't you have any NAME?")

# Pass Code Mechanism

area = "Zigatola"
letter = input("Enter Character(s): ")

if letter in area:
    print("{} is in {}".format(letter, area))
else:
    print("We Can't Find Your Location!")

name_1 = "Hitman"
code_1 = "007"
value_1 = input("Tell the Secret Code: ")
value_2 = input("Who Are You? ")

if value_1 == code_1 and value_2 == name_1:
    print("You Are Back, {}!".format(name_1))
else:
    print("You Are Not Real!")

activity = input("What Would You Like To Use For Your Data Set-Up? ")

if "Exploration" not in activity:
    print("Go Back, Read Methodology")
else:
    print("Use Exploratory Method To Find Out The Real-Time Security Threats in {0} only on {1} ".format(area, day_1))

