class Jumper:
    """This class is responsible for handling the actions of the player.
    It will facilitate the guessing and if the game is still playable.

    Stereotype: Information Holder, Service Provider

    Attr:
        guess (character): the letter guessed by the jumper.
        lives (number): how many lives the jumper still has.
    """
    def __init__(self):
        """Constructor of the Jumper class

        Args:
            self (Jumper): An instance of the Jumper class
        """
        self.guess = ""
        self.lives = 4

    def guessALetter(self):
        """Method in charge of prompting the jumper which letter they will
        guess.

        Args:
            self (Jumper): An instance of the Jumper class
        """
        self.guess = input("Guess a letter [A-Z]: ")

    def getGuess(self):
        """Method in charge of passing the letter guessed by the jumper.

        Args:
            self (Jumper): An instance of the Jumper class
        """
        return self.guess

    def updateLives(self, correct):
        """Method in charge of updating the number of lives the jumper still has
        depending on their guess.

        Args:
            self (Jumper): An instance of the Jumper class
            correct (boolean): Determines if the guess is correct or not
        """
        if not correct:
            self.lives -= 1
    
    def getLives(self):
        """Method in charge of passing the number of lives the jumper still has

        Args:
            self (Jumper): An instance of the Jumper class
        """
        return self.lives