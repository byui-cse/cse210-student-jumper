class Parachute:

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Parachute): an instance of Parachute.
        """
        self.num_wrong_guess = 0
        self.parachute_graphics = ["  ___",
                                   " /___\\",
                                   " \\   /",
                                   "  \\ /",
                                   "   0",
                                   "  /|\\",
                                   "  / \\",
                                   "\n",
                                   "^^^^^^^"]        
    
    def parachuter(self):
        if self.num_wrong_guess is not 4:
            skip = "\n".join(self.parachute_graphics[self.num_wrong_guess:])
            return skip
        
        end = "   X\n" + "\n".join(self.parachute_graphics[self.num_wrong_guess + 1:])
        return end
    
    def guessed_wrong(self):
        self.num_wrong_guess = self.num_wrong_guess + 1
    
    def end(self):
        max_guess = self.num_wrong_guess >= 4
        return max_guess
