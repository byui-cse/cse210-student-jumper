from game.jumper import Jumper
from game.player import Player
from game.puzzle import Puzzle
from game.console import Console


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.jumper = Jumper()
        self.player = Player()
        self.puzzle = Puzzle()
        self.keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
            Args:
            self (Director): an instance of Director.
          """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
  
    def get_inputs():
        """this is going to get the inputs, what letter is chosen,  from player
        from puzzle. 

            Args:
            self (Director): an instance of Director.
        """
        pass

    def do_updates():
        """ this is going to update game play, was the guess right or wrong?
        does a line get cut, or do you get to guess again
        
          Args:
            self (Director): an instance of Director.  
        """

        pass

    def do_outputs():
        """This shows the answer on the lines, and cuts or doesn't cut the string in the picture
        gives "you chose poorly" or "you chose well" type messages
        
        Args:
            self (Director): an instance of Director.
        """

        pass
