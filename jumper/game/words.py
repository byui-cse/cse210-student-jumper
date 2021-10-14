class Words:
    def __init__(self):
        self.user_letter = ['_']

    def can_guess(self, user_input):
        if user_input not in self.user_letter:
            self.user_letter.append(user_input)
            return True
        else:
            return False