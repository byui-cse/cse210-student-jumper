class Jumper:
    """drawing, remove parts, 
    random word, check agenst guesser"""
    
    def __init__(self):
        word_list = []
        word_letter = []
        pass

    

    def update_parachute(self, removeline):
        """make changes
        output list of strings
daniel"""
        parachute_man = [" ___", "/___\\", "\   /", " \ /" ,"  O", "/ | \\", " / \\"]
        return "\n".join(parachute_man)

    def choose_word(self):
        """choose word, translate to list

        output word in list form
hidi"""
        pass

    def blank_word(self):
        """ make copy of wordlist from choose word change to all blanks
        
        output list of underscores
hidi"""
        pass

    def update_blank_list(self):
        """update blank word
        output list
ben"""
        pass


    def check_guess(self, letter_list, guess):
        """is guess in letter list
        output boolian
morgan"""
        if guess in letter_list:
            return True
        else:
            return False