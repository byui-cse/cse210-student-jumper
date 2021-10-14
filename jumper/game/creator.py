import random

class Creator():
    """
    This class handles everything to do with the word. It generates a random word, returns that random word as a list of underscores, determines if the guessed letter is in the word, and edits that word as letters are guessed.

    Attributes
    self.words: A list of words that can be used with a random number as an index to determine the word.
    self.word: This is where the current word being used for the game is stored.
    self.hidden: This is a list with underscores corresponding with each letter of the word. This list is updated with the guessed letters.
    self.random: Stores a random.rand_int to determine which word to be used.

    Functions
    self.letter_in_word(letter): Accepts the argument "letter" and determines if that letter is used in the word. Returns true or false depending on if the letter is in the word.
    self.edit_hidden(letter): This function is called when a letter is guessed correctly. It accepts the argument "letter" and reveals which underscores in self.hidden contains that letter.
    """

    # Don't forget comments for methods (part of the requirements)
    # Don't forget to add your name to the README.md (part of the requirements)

    # We talked about having David and Ben do this portion
    # To enhance the game, we could use an external file as our word list
    # https://www.mit.edu/~ecprice/wordlist.10000


    def __init__(self):
        pass


    def letter_in_words(self,letter):
        pass


    def edit_hidden(self,letter):
        pass

