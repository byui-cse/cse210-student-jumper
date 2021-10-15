from game.wordProcessor import WordProcessor


class Jumper:
    """A class dedicated to printing the jumper and keeping track of points."""
    def __init__(self):
        """The class constructor.

        keepPlaying: Bool to keep track of whether the user has lost
        wrongGuess: counter to keep track of wrong guesses
        processor: an instance of the word processor class
        asciiart: a list to build the jumper art
        """
        self.keepPlaying = True
        self.wrongGuess = 0
        self.processor = WordProcessor()
        self.asciiArt = []
        self.asciiArt.append('  ___ ')
        self.asciiArt.append(" /___\\")
        self.asciiArt.append(' \\   /')
        self.asciiArt.append('  \\ /')
        self.asciiArt.append('   0   ')
        self.asciiArt.append('  /|\\  ')
        self.asciiArt.append('  / \\  ')
        self.asciiArt.append('\n^^^^^^^')
        

    def printJumper(self):
        """Method for printing the jumper in ASCII art.
        
        Args:
            self(Jumper): an instance of the jumper class
        """
        for line in self.asciiArt:
            print(line)

    def checkCorrect(self, letter):
        """Method for checking if the user's guess is correct.
        
        Args:
            self(Jumper): an instance of the Jumper class.
            letter: the letter guessed by the user.
        """
        if (not self.processor.checkLetter(letter)):
            self.wrongGuess += 1
            self.asciiArt.remove(0)
    
    def continuePlay(self, letter):
        """Method for checking if the game is gameover.
        
        Args:
            self(Jumper): Object of the Jumper class.
            letter: Guess from the user.
        """
        if letter == '  0  ':
            self.asciiArt[0] = '  X  '
            self.keepPlaying = False