import random
import os
import re


class Generator:
    """The generator class, a random word generator from a list created from a
    .txt file
    """
    def __init__(self):
        """The class constructor.

        Args:
        self (Generator): an instance of Generator.
        """
        self.game_word = self.random_word().upper() # Newly generated random word in ALL CAPS

        print(self.game_word)


    def read_doc(self):
        """Accesses the document and stores its text (lowercase format) into the
        initial_list
        """
        with open(os.path.join(os.path.dirname(__file__),'poe_raven.txt'), 'r') as data:
            self.initial_list = data.read().lower()

        return self.initial_list


    def split_doc(self):
        """Splits the initial_list into strings and stores the result into another
        list called split_list
        """
        self.split_list = re.split(r"[-_.,;:!?\"|+=@#$%^&*(){}<>~`/\[\]\\0123456789 \n]", string = self.read_doc())

        return self.split_list


    def remove_contractions(self):
        """Trims any contractions from the split_list and stores the result
        into another list called new_list
        """
        contractions = [ # general list of all accepted english language contractions
            "a'ight",
            "ain't",
            "amn't",
            "arencha",
            "aren't",
            "‘bout",
            "cannot",
            "can't",
            "cap’n",
            "'cause",
            "’cept",
            "could've",
            "couldn't",
            "couldn't've",
            "dammit",
            "daren't",
            "daresn't",
            "dasn't",
            "didn't",
            "doesn't",
            "don't",
            "dunno",
            "d'ye",
            "e'en",
            "e'er",
            "'em",
            "everybody's",
            "everyone's",
            "fo’c’sle",
            "’gainst",
            "g'day",
            "gimme",
            "giv'n",
            "gonna",
            "gon't",
            "gotta",
            "hadn't",
            "had've",
            "hasn't",
            "haven't",
            "he'd",
            "he'll",
            "helluva",
            "he's",
            "here's",
            "how'd",
            "howdy",
            "how'll",
            "how're",
            "how's",
            "I'd",
            "I'd've",
            "I'll",
            "I'm",
            "Imma",
            "I'm'o",
            "innit",
            "Ion",
            "I've",
            "isn't",
            "it'd",
            "it'll",
            "it's",
            "Iunno",
            "kinda",
            "let's",
            "ma'am",
            "mayn't",
            "may've",
            "methinks",
            "mightn't",
            "might've",
            "mustn't",
            "mustn't've",
            "must've",
            "‘neath",
            "needn't",
            "nal",
            "ne'er",
            "o'clock",
            "o'er",
            "ol'",
            "oughtn't",
            "‘round",
            "'s",
            "shalln't",
            "shan't",
            "she'd",
            "she'll",
            "she's",
            "should've",
            "shouldn't",
            "shouldn't've",
            "somebody's",
            "someone's",
            "something's",
            "so're",
            "so’s",
            "so’ve",
            "that'll",
            "that're",
            "that's",
            "that'd",
            "there'd",
            "there'll",
            "there're",
            "there's",
            "these're",
            "these've",
            "they'd",
            "they'll",
            "they're",
            "they've",
            "this's",
            "those're",
            "those've",
            "'thout",
            "’til",
            "'tis",
            "to've",
            "'twas",
            "'tween",
            "'twere",
            "'tweren't",
            "wanna",
            "wasn't",
            "we'd",
            "we'd've",
            "we'll",
            "we're",
            "we've",
            "weren't",
            "whatcha",
            "what'd",
            "what'll",
            "what're",
            "what's",
            "what've",
            "when's",
            "where'd",
            "where'll",
            "where're",
            "where's",
            "where've",
            "which'd",
            "which'll",
            "which're",
            "which's",
            "which've",
            "who'd",
            "who'd've",
            "who'll",
            "who're",
            "who's",
            "who've",
            "why'd",
            "why're",
            "why's",
            "willn't",
            "won't",
            "wonnot",
            "would've",
            "wouldn't",
            "wouldn't've",
            "y'all",
            "y'all'd've",
            "y'all'd'n't've",
            "y'all're",
            "y'at",
            "yes’m",
            "yessir",
            "you'd",
            "you'll",
            "you're",
            "you've"
            ]

        for i in range(len(contractions)):
            contractions[i] = contractions[i].lower()

        self.new_list = []

        for string in self.split_doc():
            if string in contractions:
                pass
            else:
                self.new_list.append(string)

        return self.new_list


    def final_list(self):
        """Trims the new_list to only include words with 4 or more letters and
        stores the result into another list called used_list
        """
        self.new_list = self.remove_contractions()

        self.used_list = []

        for string in self.new_list:
            if len(string) > 3:
                self.used_list.append(string)

        return self.used_list

    
    def random_word(self):
        """Selects a random word from the used_list and stores the value in
        chosen_random
        """        
        self.chosen_random = random.choice(self.final_list())

        return self.chosen_random