for i in range(1,20):
    for j in range(1,20):
        print("{0} times {1} is {2}".format(j, i, i*j))
    print("------------")

numbers = [1, 23, 31, 45, 61, 93]

for number in numbers:
    number % 8 == 0
    print("The Numbers are Unacceptable")
    break
else:
    print("No One")

