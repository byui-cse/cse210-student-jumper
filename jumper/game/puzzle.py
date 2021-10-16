import random
import linecache

class Puzzle:

    def __init__(self, wordlist='../data/mit-wordlist.txt', min_chars=2):
        self.wordlist = wordlist
        self.min_word_chars = min_chars

        with open(wordlist, 'r') as wordlist_file:
            self.wordlist_size = len([0 for _ in wordlist_file])
        
        self.previously_done = []
        self.choose_new_word()

    
    def choose_new_word(self):
        self.chosen_word = ''
        while (len(self.chosen_word) < self.min_word_chars) and (self.chosen_word not in self.previously_done):
            self.chosen_word = linecache.getline(self.wordlist, random.randint(0, self.wordlist_size - 1)).strip()
        self.previously_done.append(self.chosen_word)

    def get_word_line(self):
        pass
