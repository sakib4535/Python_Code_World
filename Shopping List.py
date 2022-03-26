shopping_list = ["ethereum", "bitcoin", "thether", "Nft"]

another_list  =  shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["image"]
print(shopping_list)
print(id(shopping_list))

i = j = k = l = m = another_list
print(i)
print("Adding Coin")
j.append("Token")
print(j)

current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Mother Board")
        elif current_choice == '2':
            computer_parts.append("Key Board")
        elif current_choice == '3':
            computer_parts.append("Mouse")
        elif current_choice == '4':
            computer_choice.append("Monitor")
    else:
        print("1: SSD")
        print("2: GPU")
        print("3: Harddisk")
        print("4: Ram")
        print("0: To Finish")

    current_choice = input("Put down the choice: ")

print(computer_parts)


i_1 = input("put down number: ")
for i in range(400,10000):
    while 400 < i <= 10000 and i % 6 == 0 :
        print ("You have unlocked visible values {} $$".format(i))
        i = i + 560
        break
    if i > 10000 and i < 400:
        print("Job Done")
    elif i % 5 == 1:
        print("Good Choice")
    else:
        print("You Must Follow the Rule of 769")
        break

enter = input("put your number: ")

for enter in range (1000,2000):
    if enter // 8 and 1000 <= enter <= 2000:
        print("Your {} Value is Now Yours".format(enter))
        break

print("Have a Good day")




