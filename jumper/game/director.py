from game.console import Console
from game.word import Word
from game.parachute import Parachute


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        parachute: Will take care of the graphics.
        console: Dictates user input and return a result.
        words: Will take of getting a random word and respond to user inputs.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.word = Word()
        self.parachute = Parachute()        
        self.keep_playing = True        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.do_outputs()
        
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()

    def do_outputs(self):
        print(self.word.secret_word())
        print(self.parachute.parachuter())
        
        self.keep_playing = not self.parachute.end() or self.word.see_blank()

    def get_inputs(self):
        user_guess = self.console.get_user_guess("Guess a letter [a-z]: ")
        
        while self.word.verify_letter(user_guess) == False:
            print("Please enter a different letter.")
            user_guess = self.console.get_user_guess("Guess a letter [a-z]: ")
        
        if self.word.letter_in_list(user_guess) == False:
            self.parachute.guessed_wrong()
