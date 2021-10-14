class Words:
    def __init__(self):
        self.user_letter = ['_']

    def can_guess(self, userInput):
        if userInput not in self.user_letter:
            self.user_letter.append(userInput)
            return True
        else:
            return False