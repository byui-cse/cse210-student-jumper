from game.jumper import Jumper
from game.wordList import WordList
from game.wordProcessor import WordProcessor
from game.wordList import WordList

class Director:
    """Director class to direct all the aspects of the game."""
    
    def __init__(self):
        """Class constructor.

        jumper: An instance of the jumper class
        wordlist: an instance of the wordlist class
        wordProcessor: an instance wordprocessor class.
        """
        self.jumper = Jumper()
        self.wordList = WordList('words.txt')
        self.wordProcessor = WordProcessor()

    def startGame(self):
        """A method to display the starting screen of the game.
        
        Args: 
            self(Director): An instance of the Director class.
        """
        self.wordProcessor.printWord()
        self.jumper.asciiArt()

    def get_updates(self):
        """A method to get the updates and run the game.
        
        Args:
            self(Director): An instance of the Director class.
        """
        while self.wordProcessor.checkWin() == False and self.jumper.continuePlay() == True:
            guess_letter = self.wordProcessor.get_letter()
            self.wordProcessor.checkLetter(guess_letter)
            self.jumper.checkCorrect(guess_letter)

            self.wordProcessor.printWord()
            self.jumper.asciiArt()