class Guesser:
    """make guess"""

    def make_guess(self):
        """Returns a letter between a-z.

        Args:
            self (Guesser): an instance of Guesser.
        """
        letter = input("Guess a letter [a-z]: ")
        return letter
