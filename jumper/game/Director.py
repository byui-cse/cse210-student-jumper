from game.player import Player
from game.board import Board
from game.generator import Generator

class Director:
    """
    Code for the director of the game
    """
    def __init__(self):
        """
        Class constructor
        """
        self.keep_playing = True
        self.player = Player()
        self.generator = Generator()
        self.word = self.generator.game_word
        self.guess = [None]*len(self.word)
        self.letter = ""
        pass
    def start_game(self):
        """
        Start the game
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        pass
    def get_inputs(self):
        """
        Get inputs from the user
        """
        self.letter = self.input("Guess a letter [a-z]: ")
    def do_updates(self):
        """
        Do updates, between inputs and outputs
        """
        # Fill up guess list
        if((self.letter in self.word) and (self.letter not in self.guess)):
            for idx, item in enumerate(word):
                if item == self.letter:
                    guess[idx] = self.letter
        # Check if we can still play
        if self.player.score == 0:
            keep_playing = False
        pass
    def do_outputs(self):
        """
        Show outputs to the user
        """
        board.show() # Show ascii art
        pass