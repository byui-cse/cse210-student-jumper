from game.jumper import Jumper
from game.wordList import WordList
from game.wordProcessor import WordProcessor

class Director:
    
    def __init__(self):
        self.jumper = Jumper()
        self.wordList = WordList('words.txt')
        self.wordProcessor = WordProcessor()

    def startGame(self):
        self.wordProcessor.printWord()
        self.jumper.printJumper()