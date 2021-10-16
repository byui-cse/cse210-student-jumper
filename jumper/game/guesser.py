class Guesser:
    """A code template for the guesser who tries to figure out the word. 
    The responsibility of this class of objects is to guess the word before
    the jumper loses all the strings of their parachute.
    
    Stereotype:
        Information Holder

    Attributes:
        Useless, . . . maybe.
    """

    def make_guess(self):
        """Returns a letter between a-z.

        Args:
            self (Guesser): an instance of Guesser.
        """
        letter = input("Guess a letter [a-z]: ")
        return letter
