class Guesser:

    def __init__(self, lives = 0):
        ''' the class contructor, keeps track of lives when intiated

        Args:
            seld(Guesser): an instance of Guesser
        '''
        self.lives = lives


    def make_guess(self):
        ''' Requests guess form user, returns user_guess to the call

        Args:
            seld(Guesser): an instance of Guesser
        '''
        
        self.user_guess = str(input('Guess a Letter [a-z]: '))

        return self.user_guess