from game.jumper import Jumper
from game.wordList import WordList
from game.wordProcessor import WordProcessor

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