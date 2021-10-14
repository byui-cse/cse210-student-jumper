import random
import re

class Word:

    def __init__(self):
        """The class constructor.
        Args:
            self (Word): an instance of Word.
        """
        self.words = ["dictionary"]
        self.chosen_word = self.random_word()
        self.letter_guessed = ["_"]
        self.blank_word = ["_"] * len(self.chosen_word)

    def random_word(self):
        self.chosen_word = random.choice(self.words)
        return self.chosen_word

    def letter_in_list(self, user_guess):
        return user_guess in self.chosen_word

    
