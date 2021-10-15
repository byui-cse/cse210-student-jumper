from game.console import Console
from game.get_word import SecretWord
from game.parachuter import Parachuter


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        console (Console): An instance of the class of objects known as Console.
        secret_word (Secretword): An instance of the class of objects known as Secretword.
        parachuter (Parachuter): An instance of the class of objects known as Parachuter.
        welcome (Welcome): An instance of the class of objects known as Welcome.
        bye (Bye): An instance of the class of objects known as Bye.
        keep_playing (boolean): Whether or not the game can continue.
        letter (string): A string containing the input character.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.secret_word = SecretWord()
        self.parachuter = Parachuter()
   