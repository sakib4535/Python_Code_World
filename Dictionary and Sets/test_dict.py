vehicle = {
    "passion": "Suzuki Gixxer 38.2",
    "dream" : "Marcedez Benz 29.0",
    "virago": "Yamaha 365",
    "fiesta": "Honda R78",
    "tenet": "Ferrari 620",
    "er5": "Lotus F679"
}

print(vehicle)

my_car = vehicle["tenet"]
print(my_car)

tonight = vehicle.get("fiesta")
print(tonight)

vehicle["roadfighter"] = "Bugatti Veron"
vehicle["learjet"] = "Lotus 313"
vehicle["toy"] = "Glider"

#update virago product (this will take place in list)
vehicle["virago"] = "Honda 656"

del vehicle["toy"]

result = vehicle.pop("f1", "You wish to exchange a racing car")
print(result)
plane = vehicle.pop("learjet", "Not Granted")
print(plane)
print()

bike = vehicle.pop("tenet", "Not present")
print(bike)

for key in vehicle:
    print(key, vehicle[key], sep=", ")

for key, value in vehicle.items():
    print(key, value, sep=", ")