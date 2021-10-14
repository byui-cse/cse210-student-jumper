from game.console import Console
from game.secretword import Secretword
from game.parachuter import Parachuter
from game.welcome import Welcome
from game.bye import Bye
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

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
        self.secret_word = Secretword()
        self.parachuter = Parachuter()
        self.welcome = Welcome()
        self.bye = Bye()
        self.keep_playing = True
        self.letter = ''


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.

        Attributes:
            os.system("cls"): Interacts with the operating system to clear the terminal
            console.write(): Displays text
            word_chart, wrong_letter: Displays the worng letter guessed by the player
            keep_playing: Loop to determine if game can continue or not
            secret_word.guess_done(): Determines if player has won the game
            else: If player loses, display message and what the secret word was
        """
        os.system("cls")
        self.console.write(self.welcome.message)
                        
        word_chart, wrong_letter = self.secret_word.show_letters()
        self.console.write("\n" + word_chart)
        
        self.console.write(self.parachuter.ascii_art[len(self.secret_word.wrong_letters)])
        
        """main loop of the game"""
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        if self.secret_word.guess_done():
            self.console.write("\nCongrats! You found the secret word and saved the jumper!")
        else:
            self.console.write(
                f"\nI'm sorry, you lost! The secret word was: {self.secret_word.word}. Better luck next time!")
        
                             
        self.console.write(self.bye.message)


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case, ...
        Args:
            self (Director): An instance of Director.
        Attributes:
            valid_letter: determine if letter guessed is a valid english letter or not
            self.letter: Asks for an input from the player
            console.write: Displays a message
        """
        valid_letter = False
        while not valid_letter:
            
            self.letter = self.console.read('\nGuess a letter (a-z): ').lower()
            valid_letter = 'a' <= self.letter <= 'z' and len(self.letter) == 1
            if not valid_letter:
                
                self.console.write('Error, \"letter\" should be a single character of the English alphabet (a-z)')
                
            else:
                valid_letter = self.letter not in self.secret_word.word_chart + self.secret_word.wrong_letters
                if not valid_letter:
                    
                    self.console.write("You have already guessed that letter, try a different one.")
           

    def do_updates(self):
        """Updates the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        Attributes:
            self.letter: Variable input from the player
            secret_word.word: The list containing the secret word
            console.write: Displays a message
            index: contains each letters index from the secret word
            letter_word: conatians each letter from the secret word
            enumarate(): loops over the iterable object
            secret_word.word_chart[index]: replaces the index in the list with the letter
            secret_word.wrong_letters: Contains list of wrong letters guessed
            parachuter.ascii_art: list of the art for the jumper in the interface
            secret_word.guess_done(): Determines if player has guessed the secret word
            keep_playing: Determines if game should continue or not
        """
        
        if self.letter in self.secret_word.word:
            self.console.write("\nGreat! You guessed a correct letter! You are a step closer to figuring out the secret word!")
            
        else:
            self.console.write("\nOh no! That letter is not in the secret word. One of the Jumper's lines has been cut!")
            self.secret_word.wrong_letters.append(self.letter) 

        
        for index, letter_word in enumerate(self.secret_word.word):
            if self.letter == letter_word:
                self.secret_word.word_chart[index] = self.letter

        if len(self.secret_word.wrong_letters) >= len(self.parachuter.ascii_art) - 1 or self.secret_word.guess_done():
            self.keep_playing = False
                
                
    def do_outputs(self):
        """Outputs the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        Attributes:
            word_chart, wrong_letter: variable that stores the value of the worng letters guessed
            console.write(): Displays text and variables
            parachuter.ascii_art: Displays the correct art of the jumper according to the number of worng letters guessed
        """
        word_chart, wrong_letter = self.secret_word.show_letters()
        self.console.write("\n" + word_chart)
        self.console.write("\n\nWrong Letters: " + wrong_letter)
        
        self.console.write(self.parachuter.ascii_art[len(self.secret_word.wrong_letters)])