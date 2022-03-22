area_list = ["Dhanmondi", "Hazaribag", "Modhubazar", "Tenari", "Lalmatia"]

for item in area_list:
    if item != "Hazaribag":
        print("Go for " + item)

for item in area_list:
    if item == "Tenari":
        continue
    print("Looking " + item)

area_find = "Lalmatia"
found_at = None

for index in range(len(area_list)):
    if area_list[index] == area_find:
        found_at = index
        break
print("{} area has been Unlocked".format(found_at))
