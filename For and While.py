i = int(input("Enter the Position Number: "))

for i in range (1,50):
        print("Break The Number is {} ".format(i))
else:
    print("Now Get the Actual Number")

# While

i_1 = 0
while i_1 < 10:
    print("i is now {}".format(i_1))
    i_1 += 1

available_exits = ["North", "East", "West", "South"]
chosen_exit = " "

chosen_exit = input("Enter the Exit-Point: ")
while chosen_exit not in available_exits:
    if chosen_exit != available_exits:
        print("Your Inside Server is Secured and Protected From the Breaches")

#Another Example

i_1 = 0
while i_1 < 10:
    print("i is now {}".format(i_1))
    i_1 += 1

available_exits = ["North", "East", "West", "South"]
chosen_exit = " "

chosen_exit = input("Enter the Exit-Point - 2: ")
while chosen_exit not in available_exits:
    chosen_exit = input("Please Choose the Right Direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Aren't you Glad?")





