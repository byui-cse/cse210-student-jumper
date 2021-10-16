from game.get_word import SecretWord

'to verify that the guessed letter is in the word or not and return a true or false value'


class verify:

    def __init__(self):
        """The class constructor.

        Args:
        self (verify): an instance of Director.
    """

    self.secret_word = SecretWord()

    def check_letter(self):
        if guess in self.secret_word:
            return True
        elif guess not in self.secret_word:
            return False
