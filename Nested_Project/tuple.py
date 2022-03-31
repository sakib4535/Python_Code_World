list = ["pistol", "rifle", "Sniper"]
a = ["Machine Gun", "Bomb"]
list_1 = list.extend(a)
print("You got now {} {}".format(list, "$$@@"))

number = [12, 7.2, 11.1, 18.2, 5, 10.12]
print(sum(number))
print(max(number))
print(min(number))

max_value = 18
min_value = 5
number_sort = sorted(number)

for index in range(len(number_sort)):
    if number_sort[index] > max_value or number_sort[index] < min_value:     #(Need Some Work)
        print(number_sort, index)
        del number_sort[index]

print(number)


list_str = '-'.join(list)
print(list_str)

for index in enumerate(list):
    print(index)


