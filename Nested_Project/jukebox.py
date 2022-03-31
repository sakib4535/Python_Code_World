from nested_1 import codes

while True:
    print("Choose Your Preferred Name: ")
    for index, (title, code, rate, idea) in enumerate(codes):
        print("{}: {}, {}, {}"
              .format(index + 1, title, code, rate))
    choice = int(input("Put You Choice: "))
    if 1 <= choice <= len(codes):
        code_list = codes[choice - 1][2]
    else:
        break

    print(codes[coice - 1])
    print(codes)
    print()

    for index, value in enumerate(codes):
        title, code, rate, idea = value
        print(index, title, code, rate, idea)
    break


