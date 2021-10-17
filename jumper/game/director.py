from game.jumper import Jumper
from game.player import Player
from game.puzzle import Puzzle
from game.console import Console


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.

        Stereotype:  Controller... I don't know what this means. but it is in most of the director classes I see. 

        Attributes: 
            console : an instance of the class Console
            words : an isntance of the class Puzzle

        """
        self.jumper = Jumper()
        self.player = Player()
        self.puzzle = Puzzle()
        self.console = Console()
        self.keep_playing = True
        self.letter = ""


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
            Args:
            self (Director): an instance of Director.
            Attributes: 
          """
        self.console.write(self.intro) 
        
        chosen_word_letters, _ = self.chosen_word.show_letters()
        self.console.write ( chosen_word_letters)
        self.console.write(self.Jumper.ascii_art[len(self.chosen_word.wrong_letters)])


        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
        if self.chosen_word.guess_done():
            self.console.write("you guessed the word. ")
        else:
            self.console.write(f"you died. the word was {self.chosen_word.word}")  # i dont now why I need to put .word


  
    def get_inputs():
        """this is going to get the inputs, what letter is chosen,  from player
        from puzzle. 

            Args:
            self (Director): an instance of Director.
            
            some people I looked at used this space to validate that the letters chosen were
            english letters.  I'm not sure I want to do that. 
            I think it should  point to player and get the user inputs, the ones I put in another space. 
        """
        pass

    def do_updates(self):
        """ this is going to update game play, was the guess right or wrong?
        does a line get cut, or do you get to guess again
        
          Args:
            self (Director): an instance of Director. 
            Attributes: letter_word: contains each letter in the chosen word

        """

        if self.letter in self.chosen_word.word:
            self.console.write(" you guessed correctly. next letter: ")
        else:
            self.console.write(" That letter is not in the word.  Your chute line is cut")
            self.chosen_word.wrong_letters.append(self.letter)

        for index, chosen_word_letters in enumerate(self.chosen_word.word):
            if self.letter == chosen_word_letters.word:
                self.chosen_word.chosen_word_letters[index] =self.letter

        if len(self.chosen_word.wrong_letters) >= len(self.jumper.ascii_art) -1 or self.chosen_word.guess_end():
            self.keep_playing = False        

    def do_outputs():
        """This shows the answer on the lines, and cuts or doesn't cut the string in the picture
        gives "you chose poorly" or "you chose well" type messages
        
        Args:
            self (Director): an instance of Director.
        """# I think I put some of this in do updates. 

        pass

if __name__ =="__main__":
    director = Director() 
    director.start_game()


