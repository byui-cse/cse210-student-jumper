import random

class Words:
    def __init__(self):
        self.user_letter = ['_']
        self.secret_word = self.random_word()

    def can_guess(self, user_input):
        if user_input not in self.user_letter:
            self.user_letter.append(user_input)
            return True
        else:
            return False
    
    def verify_letter(self, user_input):
        return user_input in self.secret_word
    
    def random_word(self):
        self.secret_word = random.choice(self.words)
        return self.secret_word