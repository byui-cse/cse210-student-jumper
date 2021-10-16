class State:
    """This class is responsible for drawing the interface
    based on the game status.

    Stereotype: Interfacer

    Attr:
        hint (list of char): the hint that will be displayed in the game
        lives (number): how many lives the jumper still has
    """
    def __init__(self, key):
        """Constructor of the State class

        Args:
            self (State): An instance of the State class
        """
        self.hint = []
        self.hint = key
        self.lives = 4

    def updateStatus(self, currLife, currHint):
        """Gets the current status of the game

        Args:
            self (State): An instance of the State class
            currLife (number): Current number of lives the player has
            currHint(list of char): Current state of hints the player has
        """
        self.lives = currLife
        self.hint = currHint

    def draw(self):
        """Draws the current state of the game

        Args:
            self (State): An instance of the State class
        """
        for i in range(len(self.hint)):
            print(self.hint[i], end=" ")

        if self.lives == 4:
            print()
            print("  _____   ")
            print(" /     \\")
            print(" -------")
            print(" \\     /")
            print("  \\   /")
            print("    0 ")
            print("   /|\\")
            print("   / \\")
            print()
            print("^^^^^^^^^")
        elif self.lives == 3:
            print()
            print(" /     \\")
            print(" -------")
            print(" \\     /")
            print("  \\   /")
            print("    0 ")
            print("   /|\\")
            print("   / \\")
            print()
            print("^^^^^^^^^")
        elif self.lives == 2:
            print()
            print(" \\     /")
            print("  \\   /")
            print("    0 ")
            print("   /|\\")
            print("   / \\")
            print()
            print("^^^^^^^^^")
        elif self.lives == 1:
            print()
            print("  \\   /")
            print("    0 ")
            print("   /|\\")
            print("   / \\")
            print()
            print("^^^^^^^^^")
        elif self.lives == 0:
            print()
            print("    X ")
            print("   /|\\")
            print("   / \\")
            print()
            print("^^^^^^^^^")