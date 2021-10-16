from game.jumper import Jumper
from game.console import Console
from game.guesser import Guesser

class Director:
    """A code template for a person who directs the game. The responsibility 
    of this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        guesser (Guesser): An instance of the class of objects known as Guesser.
    """

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
        parachute = self.jumper.parachute_man
        self.console.write(self.jumper.display_parachute())
        self.word = self.console.read('Guess a letter [a-z]: ')
        self.jumper.update_blank_list(self.word)

        pass

    def do_updates(self):
        """call check guess update list and parachute
        Author: Mitchell"""
        self.jumper.check_guess(self.jumper.word_list,self.guesser.make_guess()) 
            # second argument should be changeed to self.guesser.(whatever attribute is defined in the guesser init)
            # first argument should work when word_list is used in the jumper class.  

    def do_outputs(self):
        """display data
        morgan"""
        blank_word = self.jumper.update_blank_list()
        paratute = self.jumper.update_parachute()
        self.console.write(paratute)
        self.console.write(blank_word)