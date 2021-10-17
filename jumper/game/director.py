from game.console import Console
from game.generate_word import Word
from game.lives import Lives
from game.puzzle import Puzzle


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        puzzle (Puzzle): An instance of the class of object known as Puzzle
        live (Lives): An instance of the class of object known as Lives. It is reponsible for the lives of the player/guesser
        word (Word): An instance of the class of objet known as Word. Generate random word
        lives (int): to store the lives of the
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director
        """

        self.console = Console()
        self.keep_playing = True
        self.puzzle = Puzzle()
        self.live = Lives()
        self.word = Word()
        self.lives = self.live.lives

    def start_game(self):
        """Stats the game loop to control the sequence of play.

        
        Args:
            self (Director): an instance of Director.
        """
        word = self.word.random_word()
        print(word)
        self.puzzle.set_word(word)
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.end_game_message()
        
    def get_inputs(self):
        """Get the inputs at the beginning of each round of play. In this case,
        that means asking the guesser for another letter.

        Args:
            self (Director): An instance of Director.
        """
        
        interface = self.puzzle.interface(self.lives)
        for i in interface:
            self.console.write(i)
        letter = self.console.read(self.puzzle.question())
        evaluation = self.puzzle.evaluate(letter)
        self.live.lives_counter(evaluation)

    def do_updates(self):
        """Updates the value of keep_playing parameter to stop the game when the lenght of list parachute_man is equal to six

        Args:
            self (Director): An instance of Director.
        """
        self.console.clear()
        if len(self.puzzle.parachute_man) == 7:
            self.keep_playing = False
            for i in self.puzzle.dead_man:
                self.console.write(i)
    
    def end_game_message(self):
        """Display text if the player guess the correct puzzle
        Args:
            self (Director): An instance of Director
        """
        
        if len(self.puzzle.word) == self.puzzle.progress:
            self.console.write(self.puzzle.survivor_man())
            self.keep_playing = False

    
