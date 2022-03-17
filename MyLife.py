my_un = "Hasnain Imtiaz Sakib"
print(my_un[0:3] + my_un[4] + my_un[3] + ", He's Guilty ")
print(my_un[2])
print(my_un[5])
print(my_un[6])
print(my_un[-5:-2])
print(my_un[0:8:4])
print(my_un[0:6:3])

number = "90,112,234,413,566"
seperator =  number[2::4]
print(seperator)

values = "".join(char if char not in seperator else "" for char in number).split()
print([int(val) for val in values])

#Slicing Backward
name = "Hasnain Imtiaz Sakib"
print(name[17:0:-1])
print(name[17::-1])
print(name[::-1])

str1 = "sakib "
str2 = "gama "
str3 = "alpha "

print(str1 + str2 + str3)
print(str1 * 4)

today = 'friday'
print('day' in today) #True
print('fiy' in today) #False

age = 27
print("My age is {0} years ".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}".format(31, "Jan", "Feb", "Mar", "Apr") )
print("""Jan: {2}
Feb: {0}
March: {2}
April: {1}""".format(28,30,31))

age = 22
print(name + f" is {age} years old")

name = input("What is Your Name: ")
age = int(input("What is Your Age, {0}? ".format(name)))
IQ = int(input("Your IQ Level: ". format(name)))
print("You have {0} IQ level while you are {1} Years Old ". format(IQ,age))

if IQ <= 5 and age >= 18:
    print("You must leave the planet\nBecause you are not dependable\nyou should practice more and more")
else:
    print("Please! You are Welcome Mr. Furious")
if IQ >= 5:
    print("We are looking for you MR. Dependable\nIt will be very much pleasure to Work with you!")
else:
    print("Go back Your Position and Start Working!!!")

# Guess The Right Answer (IQ Level)
answer = 5

print("guess the Number between 1 to 10: ")
guess = int(input())

if guess > answer:
    print("Please guess the Lowest Number again" + " (Last Chance)")
    guess = int(input())
    if guess == answer:
        print("Well Done, You are Right!")
elif guess < answer:
    print("Please guess the Highest Number again" + " (Last Chance)")
    guess = int(input())
    if guess == answer:
        print("Well Done, You are Right!")
else:
    print("Your Guess is Right!\nYou are Genius!\n You Guessed it First Time!")







