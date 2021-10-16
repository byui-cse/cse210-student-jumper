import random

class Jumper:
    """drawing, remove parts, 
    random word, check against guesser"""

    """The class holder for methods and attributes associated with the 
    jumper. The responsibility of this class of objects is to provide 
    the parachute, removing lines as letters are guessed, provide the 
    mystery word, and check answers against the guesser.
    
    Stereotype:
        Information Holder

    Attributes:
        word_list (list): The word the guesser must figure out.
        word_letters (integer): The number of letters in the word.
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.word_list = []
        self.word_letters = set(self.word_list)  # letters in the word

    def update_parachute(self, removeline):
        """make changes
        output list of strings
daniel"""
        parachute_man = [" ___", "/___\\", "\   /", " \ /" ,"  O", "/ | \\", " / \\"]
        return "\n".join(parachute_man)

    def choose_word(self):
        """choose word, translate to list

        output word in list form
heidi"""

        """Chooses a random word from word_list for the guesser.

        Args:
            self (Jumper): An instance of Jumper.
        """

        self.word_list = ["honest", "partnership", "hostile", "copyright", "missile", "chance", "cellar", "spokesperson", "license", "economic", "follow", "momentum", "supply", "rainbow", "capricious", "emblazon", "featherbrained", "nuance", "wearisome", "majestic", "whimsical", "twaddle", "fungus", "gemstone", "hieroglyph", "jumble", "kaleidoscope", "mosquito", "pendulum", "signature", "spectrum", "thermometer", "vacuum", "nauseating", "zonked", "functional", "jewel", "lavish", "wandering", "fascinated", "illustrious", "scribble", "invincible", "colossal", "spiteful", "aspinring", "soggy", "hypnotic", "quirky", "mellow", "pricey", "gruesome", "earsplitting", "fallacious", "protective", "authority", "overrated", "measely", "mountainous,", "exclusive", "statuesque", "vivacious", "apathetic", "oafish", "ubiquitous", "lighten", "imaginary", "knotty", "futuristic", "astonishing", "flagrant", "humdrum", "boorish", "phobia", "highfalutin", "parched", "bustling", "condition", "cuddly", "obscene", "bridge", "fuzzy", "squash", "voyager", "shipmate", "hulking", "scrawny", "woebegone", "subsequent", "poised", "efficacious", "aboriginal", "malicious", "substantial", "disillusioned", "unequaled", "existence", "jagged", "cowardly", "ferocious", "incumbent", "sulky", "sanctuary"]
        self.word = random.choice(self.word_list)
        # print(self.word)

    def blank_word(self):
        """ make copy of wordlist from choose word change to all blanks
        
        output list of underscores
heidi"""
        
        """Creates blank spaces (underscores) for each letter of the selected word 
        for the guesser.

        Args:
            self (Jumper): An instance of Jumper.
        """

        num_blanks = len(self.word)
        print("Your word is " + str(num_blanks) + " letters long.") 
        blanks = [letter if letter in used_letters else ' _ ' for letter in self.word]

    def update_blank_list(self):
        """update blank word
        output list
ben"""
        pass


    def check_guess(self, letter_list, guess):
        """is guess in letter list
        output boolean
morgan"""
        if guess in letter_list:
            return True
        else:
            return False