part_lists = {"1": "computer",
              "2": "monitor",
              "3": "HDMI",
              "4": "GPU",
              "5": "hard_disk",
}

current_choice = None
while current_choice != "0":
    if current_choice in part_lists:
        chosen_part = part_lists[current_choice]
        print(f"Adding{chosen_part}")

    current_choice = input("> ")

