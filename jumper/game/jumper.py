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
        self.word_list: list of awesome words
        self.word: random word that is picked from self.word_list when the Jumper class is instantiated
        self.letter_list: list of letters created from self.word
        self.blank_list: list of blanks that will be updated according to correct guesses
        self.parachute_man: awesome parachute guy
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Jumper): An instance of Jumper.
        """

        self.word_list = [
            "honest",
            "partnership",
            "hostile",
            "copyright",
            "missile",
            "chance",
            "cellar",
            "spokesperson",
            "license",
            "economic",
            "follow",
            "momentum",
            "supply",
            "rainbow",
            "capricious",
            "emblazon",
            "featherbrained",
            "nuance",
            "wearisome",
            "majestic",
            "whimsical",
            "twaddle",
            "fungus",
            "gemstone",
            "hieroglyph",
            "jumble",
            "kaleidoscope",
            "mosquito",
            "pendulum",
            "signature",
            "spectrum",
            "thermometer",
            "vacuum",
            "nauseating",
            "zonked",
            "functional",
            "jewel",
            "lavish",
            "wandering",
            "fascinated",
            "illustrious",
            "scribble",
            "invincible",
            "colossal",
            "spiteful",
            "aspinring",
            "soggy",
            "hypnotic",
            "quirky",
            "mellow",
            "pricey",
            "gruesome",
            "earsplitting",
            "fallacious",
            "protective",
            "authority",
            "overrated",
            "measely",
            "mountainous,",
            "exclusive",
            "statuesque",
            "vivacious",
            "apathetic",
            "oafish",
            "ubiquitous",
            "lighten",
            "imaginary",
            "knotty",
            "futuristic",
            "astonishing",
            "flagrant",
            "humdrum",
            "boorish",
            "phobia",
            "highfalutin",
            "parched",
            "bustling",
            "condition",
            "cuddly",
            "obscene",
            "bridge",
            "fuzzy",
            "squash",
            "voyager",
            "shipmate",
            "hulking",
            "scrawny",
            "woebegone",
            "subsequent",
            "poised",
            "efficacious",
            "aboriginal",
            "malicious",
            "substantial",
            "disillusioned",
            "unequaled",
            "existence",
            "jagged",
            "cowardly",
            "ferocious",
            "incumbent",
            "sulky",
            "sanctuary",
        ]
        self.word = random.choice(self.word_list)
        self.letter_list = [letter for letter in self.word]
        self.blank_list = ["_" for _ in self.word]

        self.parachute_man = [
            " ___",
            "/___\\",
            "\   /",
            " \ /",
            "  O",
            "/ | \\",
            " / \\",
            "^^^^^^^^"
        ]

    def display_parachute(self):
        """output origional image of the parachute man
        daniel"""
        return "\n".join(self.parachute_man)

    def update_parachute(self):
        if len(self.parachute_man) > 3:
            self.parachute_man.pop(0)
        elif len(self.parachute_man) == 3:
            self.parachute_man[0] = "  X"
        else:
            return self.parachute_man
        


    def update_blank_list(self, letter):
        """Updates the blank list.
        Removes the correct letter from the letter_list and inserts a placeholder.
        Removes "_" from the blank_list and inserts the letter at the correct index.

        Args:
            self: (Jumper) An instance of jumper.
            letter: the guessed letter that will be passed to the method in the Director class
        """
        # get index of guessed letter
        index = self.letter_list.index(letter)

        # get correct letter
        correct_letter = self.letter_list.pop(index)

        # insert place_holder
        self.letter_list.insert(index, "_")

        # remove blank at index
        self.blank_list.pop(index)

        # insert correct letter at index
        self.blank_list.insert(index, correct_letter)

    def print_blank_list(self):
        """Prints the blank_list.

        Args:
        self: (Jumper) An instance of jumper.
        """
        # loop through each letter, strip the newline, and end each letter with a space
        for letter in self.blank_list:
            print(letter, end=" ")
        print()

    def check_guess(self, guess):
        """is guess in letter list
        output boolean
        morgan"""
        if guess in self.letter_list:
            return True
        else:
            return False
