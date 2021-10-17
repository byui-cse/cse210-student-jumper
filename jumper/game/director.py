from game.console import Console
from game.get_word import SecretWord
from game.parachuter import Parachuter
from game.Verify import Verify
import os

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        console (Console): An instance of the class of objects known as Console.
        get_word (Secretword): An instance of the class of objects known as Secretword.
        parachuter (Parachuter): An instance of the class of objects known as Parachuter.
        verify (Verify): 'to verify that the guessed letter is in the word or not and return a true or false 
        keep_playing (boolean): Whether or not the game can continue.
        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.secret_word = SecretWord()
        self.parachuter = Parachuter()
        self.verify = Verify()
        self.keep_playing = True
        self.letter = ""

    def start_game(self):
        """ Starts the game loop to control the sequence of play.
        
            Args:
            self (Director): an instance of Director.
            Attributes:
           
            keep_playing: Loop to determine if game can continue or not
            secret_word.guess_done(): Determines if player has won the game
            else: If player loses, display message and what the secret word was
        """

        """ loop """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


        
        if self.secret_word.get_word():
            self.console.write("\nCongrats! You found the secret word and saved the jumper!")
        else:
            self.console.write(
                f"\nI'm sorry, you lost! The secret word was: {self.secret_word.get_word}. Better luck next time!")

        self.parachuter.print_parachuter()

    def get_inputs(self):
        """ Gets the inputs at the beginning of each round of play. In this case, ...
            Args:
            self (Director): An instance of Director.
            Attributes:
            valid_letter: determine if letter guessed is a valid english letter or not
            self.letter: Asks for an input from the player
            console.write: Displays a message """
        self.console.get_letter
        
                    

    def do_updates(self):
        """ Updates the important game information for each round of play.
            Args:
            self (Director): An instance of Director.
            Attributes:
            self.letter: Variable input from the player
            secret_word.word: The list containing the secret word
            console.write: Displays a message"""

        if self.letter in self.verify.verify_guess(self.secret_word.myFiles):
            self.console.write("\nGreat! You guessed a correct letter! You are a step closer to figuring out the secret word!")

        else:
            self.console.write("\nOh no! That letter is not in the secret word. One of the Jumper's lines has been cut!")


    def do_outputs(self):
        """ Outputs the important game information for each round of play.
            Args:
            self (Director): An instance of Director.
            Attributes:
            console.write(): Displays text and variables
            """
        
        word_chart = self.secret_word.get_word()
        self.console.write("\n" + word_chart)

        self.console.write(self.parachuter.update_parachuter[len(self.secret_word.new_word)])