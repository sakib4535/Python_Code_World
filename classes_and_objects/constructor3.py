# Parameterized Constructor

class Games:
    def __init__(self, name, genre):
        print("This is fruit with Names")
        self.name = name
        self.genre = genre

    def show(self):
        print("The name of the game is", self.name, "and genre is", self.genre)

obj = Games("PUBG", "Online Battleground")
obj.show()

# Creating object of the class which will invoke parameterized constructor

