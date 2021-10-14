from game.parachute import Parachute
from game.console import Console
from game.words import Words

class Director:

    def __init__(self):
        """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        parachute: Will take care of the graphics.
        console: Dictates user input and return a result.
        words: Will take of getting a random word and respond to user inputs.
        """
        self.keep_playing = True
        self.parachute = Parachute()
        self.console = Console()        
        self.words = Words()    
        

    def start_game(self):        
        self.do_outputs()
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
        
        self.game_over()

    def get_inputs(self):
        user_input = self.console.get_letter("Guess a letter [a-z]: ")
        while not self.words.can_guess(user_input):
            self.console.write("Letter already guessed.")
            user_input = self.console.get_letter("Guess a letter [a-z]: ")
        if not self.words.verify_letter(user_input):
            self.parachute.wrong_guess()

    def do_outputs(self):
        