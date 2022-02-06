from game.jumper import Jumper
from game.console import Console
from game.guesser import Guesser
import random


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

        # Make these method calls to print the blank_list; print the jumper; and make a guess
        self.jumper.print_blank_list()
        self.console.write(self.jumper.display_parachute())
        self.letter = self.guesser.make_guess()

    def do_updates(self):
        """call check guess update list and parachute
        Author: Mitchell"""

        # to check if the letter is in the word and to update blank list
        if self.jumper.check_guess(self.letter):
            random_statements_positive = ['You´re not completely useless :D', 'lucky guess', 'Thats not fair!', 'Is that the best you can do?', 'Would you like buy a vowel?']
            self.jumper.update_blank_list(self.letter)
            print(random.choice(random_statements_positive))

        else:
            self.jumper.update_parachute() 
            random_statements_negative = ['Wow and you´re a college student', 'Your killing me Smalls!', 'This explains so much...', 'Did you really guess that letter?', 'You´re the worst', 'He´s dropping fast', 'CARE!!!']
            print(random.choice(random_statements_negative))

    def do_outputs(self):
        """display data
        morgan"""

        # to check if the updated blank_list matches the word you could run something like this:
        blank_word = "".join(self.jumper.blank_list)
        if blank_word == self.jumper.word:
            self.keep_playing = False
            print("You saved me!")
            

        # we also need to add logic for checking if the parachute man is dead
        if self.jumper.parachute_man[0] == "  X":
            print("death")
            self.keep_playing = False
            print(self.jumper.display_parachute())
