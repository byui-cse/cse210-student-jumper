from game.WordBank import word_bank
from game.DisplayGuy import board

class director:
    
    def __init__(self):
        """The class constructor.
     
        Args:
        self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.word_bank = word_bank()
        self.board = board()
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
                self.get_inputs()
                self.do_updates()
                self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means Dealing the card.

        Args:
        self (Director): An instance of Director.
        """
        self.board.guy()
        self.board.parachute()
        choice = input("Guess a letter a-z ")
        self.board.check_guess(choice)



    def do_updates(self):
        self.keep_playing = self.board.stayin_alive()


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the cards that were dealt and the score.

        Args:
        self (Director): An instance of Director.
        """
        if self.keep_playing == False:
            self.board.parachute()
        
        if self.board.check_win():
            self.board.parachute()
            print('You win!!')
            self.keep_playing = False
        
            
