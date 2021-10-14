from game.jumper import Jumper
from game.console import Console
from game.guesser import Guesser

class Director:
    
    def __init__(self):
        self.keep_playing = True
        self.jumper = Jumper()
        self.console = Console()
        self.guesser = Guesser()

    def start_game(self):
        while self.keep_playing == True:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """get word blanks
        get parachute
        make guessGuess a letter [a-z]:
mitchell"""
        pass

    def do_updates(self):
        """call check guess update list and parachute
mitchell"""
        pass

    def do_outputs(self):
        """display data
morgan"""
        pass