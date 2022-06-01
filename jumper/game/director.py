from creator import Creator
from jumper import Jumper
from player import Player

class Director():
    """
    This class directs the game. He relies on the creator, jumper, and player to print and evaluate information.

    Functions
    __init__: Creates an object for each class and sets keep_playing to true.
    start_game: Displays initial information, and runs while loop to play the game.
    do_inputs: Calls self.player.get_input() to get a letter as input, and stores the input
    do_updates: Calls self.creator.letter_in_words(input) to determine if the letter is in the word, and returns true/false. If true, self.creator.edit_hidden(input) is called to display where the letter is in the word. If false, self.jumper.decrease_lives and self.jumper.alter_jumper are called.
    do_outputs: Loops through the lines of self.jumper.jumper and prints each line. Then it loops through the characters of self.creator.hidden and prints them. 
    continue_game: Determine if the player can keep playing or not by checking if self.jumper.lives is equal to 0, and then setting self.keep_playing to false if they can't keep playing. Also, end the game if the word is guessed correctly by checking if self.creator.hidden doesn't contain any underscores. 
    """


    # Don't forget comments for methods (part of the requirements)
    # Don't forget to add your name to the README.md (part of the requirements)

    # Xander, will you work with me (Riley) to complete this director class?
    # Please do the following:
    # Complete the do_inputs function
    # Complete the do_updates function
    # Complete the continue_game function

    def __init__(self):
        self.creator = Creator()
        self.jumper = Jumper()
        self.player = Player()
        self.keep_playing = True


    def start_game(self):
        """
        This function displays the initial jumper and hidden word (ex. _ _ _ _ _), and then contains the while loop to run the game.
        """
        
        # To enhance the game
        self.do_outputs()
        
        while self.keep_playing:
            self.do_inputs()
            self.do_updates()
            self.do_outputs()
            self.continue_game()


    def do_inputs(self):
        # let the player know how many more lives they have
        print (f'I have {Jumper.self.lives} chances left. Please save me!')
        # Find the letter that the player is going to guess
        Player.self.get_input()
        
        

    def do_updates(self):
        # apply the guess to the current game
        if Player.self.guess == Creator.letter_in_words:
            Jumper.self.alter_jumper(Player.self.guess)
        else:
            Jumper.self.decrease_lives()


    def do_outputs(self):
        print ("")
        
        for line in self.jumper.jumper:
            print(line)
        
        print ("")

        for character in self.creator.hidden:
            print(character + " ",end="")

        print ("")

    def continue_game(self):
        # To enhance the program, display a congratulatory message, or tell them the word if they got it wrong.
        # To determain if the game contiues look at the jumper and see how many lines have been cut.
        # To determain if the game is won, see if the whole word has been discovered
        if Creator.self.hidden == Creator.self.word:
            print ('Congradulations, you win!')
            self.keep_playing = False
        elif Jumper.self.lives == 0:
            print (f'Too bad, better luck next time. Your word was {Creator.self.word}.')
            self.keep_playing = False
        else:
           pass