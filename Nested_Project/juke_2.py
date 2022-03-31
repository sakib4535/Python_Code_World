from nested_1 import codes

while True:
    print("Choose Your Preferred Name: ")
    for index, (title, code, rate, idea) in enumerate(codes):
        print("{}: {}"
              .format(index + 1, title))
    choice = int(input("Put You Choice: "))
    if 1 <= choice <= len(codes):
        code_list = codes[choice - 1][2]
    else:
        break

    print(codes[choice - 1])
    print(code_list)
    print()




