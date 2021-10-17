from game.get_word import SecretWord
import re

'to verify that the guessed letter is in the word or not and return a true or false value'


class Verify:

    def __init__(self):
        """The class constructor.

        Args:
        self (verify): an instance of Director.
    """

        self.selected_word = SecretWord()

    # this function verifies or checks if the letter is in the selected word and then returns the letter and 
# the remaining dashes. 
    def verify_guess(self, guess):
           
        x = re.finditer(f'[{guess}]+', self.selected_word)
        match = [match.start() for match in x]

        for i in match:
            self.remaining_char[i] = f'{guess}'
