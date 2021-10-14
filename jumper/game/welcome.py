class Welcome():
    """Displays the welcome message.

    Stereotype:
        Information Holder
    """
    def __init__(self) -> None:
        """The class constructor.
          
          Args:
              self (Welcome): an instance of Welcome.
        """
        self.message = """---------------------------------------------------------------------------------
Welcome to Jumper, version Team 2.
Jumper is played according to the following rules:

1. The puzzle is a secret word randomly chosen from a list.
2. The player guesses a letter in the puzzle.
3. If the guess is correct, the letter is revealed.
4. If the guess is incorrect, a line is cut on the jumper's parachute.
5. Play continues until the puzzle is solved or the jumper has no more parachute.
---------------------------------------------------------------------------------"""