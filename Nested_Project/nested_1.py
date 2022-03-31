codes = [
    ("welcome", "party", 6534,
     [
         (1, "toss the coin"),
         (2, "Open the secrets"),
         (3, "Open the Nodes"),
         (4, "Open Horkheimer"),
     ]
     ),
    ("Battlefield", "bad Company", 243421,
     [
         (1, "bad people"),
         (2, "good People"),
         (3, "Hundred Stars"),
         (4, "Rescue Mission"),
     ]
     ),
    ("Generic Idea", "Clash of Civilization", 9987,
     [
         (1, "Mash"),
         (2, "Ashe"),
         (3, "Mesh"),
         (4, "Linear"),
     ]
     ),
]

print(len(codes))

for name, code, rate, idea in codes:
    print("Blueprint: {}, Main source: {}, Identity: {}".format(name, code, rate, idea))

code_1 = codes[2]
print(code_1)
print(codes[1])

print(codes[2][3][1][0])
