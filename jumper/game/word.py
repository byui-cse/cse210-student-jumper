import random
import re

class Word:

    def __init__(self):
        """The class constructor.
        Args:
            self (Word): an instance of Word.
        """
        self.chosen_word = self.random_word()
        self.words = ["dictionary"]        
        self.letter_guessed = ["_"]
        self.blank_word = ["_"] * len(self.chosen_word)

    def random_word(self):
        self.chosen_word = random.choice(self.words)
        return self.chosen_word

    def letter_in_list(self, user_guess):
        return user_guess in self.chosen_word

    def verify_letter(self, user_guess):
        if user_guess not in self.letter_guessed:
            return self.letter_guessed.append(user_guess)
        else:
            return False

    def secret_word(self):
        for i in re.finditer(self.letter_guessed[-1], self.chosen_word):
            index = i.start()
            self.blank_word[index] = self.letter_guessed[-1]
        
        blank_word = " ".join(self.blank_word)
        return blank_word

    def see_blank(self):
        if ["_"] is not self.blank_word:
            return False
        else:
            return True
