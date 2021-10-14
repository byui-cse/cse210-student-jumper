from game.parachute import Parachute
from game.console import Console
from game.words import Words

class Director:

    def __init__(self):
        """The class constructor.
        Args:
            self (Director): an instance of Director.
        """
        self.parachute = Parachute()
        self.console = Console()
        self.keep_playing = True
        self.words = Words()    
        

    def start_game(self):        
        self.do_outputs()
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
        
        self.game_over()

    def get_inputs(self):
        userInput = self.console.get_letter("Guess a letter [a-z]: ")
        while not self.words.can_guess(userInput):
            self.console.write("Letter already guessed.")
            userInput = self.console.get_letter("Guess a letter [a-z]: ")
        if not self.words.verify_letter(userInput):
            self.parachute.wrong_guess()

    def do_outputs(self):
        