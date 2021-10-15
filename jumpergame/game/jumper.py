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
        

    def print_jumper(self):
        '''Prints ASCII art (parachute) to the terminal below the word that the user guesses 
        what letters make up the word.
        '''
        # self.asciiArt = []
        # self.asciiArt.append('  ___ ')
        # self.asciiArt.append(" /___\\")
        # self.asciiArt.append(' \\   /')
        # self.asciiArt.append('  \\ /')
        # self.asciiArt.append('   0   ')
        # self.asciiArt.append('  /|\\  ')
        # self.asciiArt.append('  / \\  ')
        # self.asciiArt.append('\n^^^^^^^')

        for line in range(len(self.asciiArt)):
            print(self.asciiArt[line])


    def checkCorrect(self, letter):
        """Method for checking if the user's guess is correct.
        
        Args:
            self(Jumper): an instance of the Jumper class.
            letter: the letter guessed by the user.
        """
        if self.processor.checkLetter(letter) == False:
            self.wrongGuess += 1
            self.asciiArt.pop(0)
    
    def continuePlay(self):
        """Method for checking if the game is gameover.
        
        Args:
            self(Jumper): Object of the Jumper class.
            letter: Guess from the user.
        """
        keep_playing = True

        if self.wrongGuess == 5:
            self.asciiArt[0] = '  X  '
            keep_playing = False
        
        return keep_playing