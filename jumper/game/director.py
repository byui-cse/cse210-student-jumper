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
        Author: Mitchell"""
        parachute = self.jumper.update_parachute()
        self.console.write(parachute)
        word = self.console.read('Guess a letter [a-z]: ')
        self.jumper.update_blank_list(word)

        pass

    def do_updates(self):
        """call check guess update list and parachute
        Author: Mitchell"""
        self.jumper.check_guess(self.jumper.word_list,self.guesser.read_response) 
            # second argument should be changeed to self.guesser.(whatever attribute is defined in the guesser init)
            # first argument should work when word_list is used in the jumper class.  
        pass

    def do_outputs(self):
        """display data
        morgan"""
        blank_word = self.jumper.update_blank_list()
        paratute = self.jumper.update_parachute()
        self.console.write(paratute)
        self.console.write(blank_word)