from game.jumper import Jumper
from game.checker import Checker
from game.state import State
import random

class director:

    """a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype: Coordinator
        """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.listOfWords = ["happy", "computer", "family", "gospel", "internet", "love"]
        self.jumper = Jumper()
        self.checker = Checker(random.choice(self.listOfWords))
        self.state = State(self.checker.get_hint())


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            gets update from jumper
        """
        self.state.draw()
        while self.jumper.getLives() > 0 and not self.checker.isFinished():
            self.get_inputs()
            self.updates()
            self.displayOutput()


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        self.jumper.guessALetter()

    def updates (self):
        self.checker.checkAnswer(self.jumper.getGuess())
        self.jumper.updateLives(self.checker.isCorrect())
        self.state.updateStatus(self.jumper.getLives(), self.checker.get_hint())
    
    def displayOutput(self):
        self.state.draw()