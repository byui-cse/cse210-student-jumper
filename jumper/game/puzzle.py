import random

class Puzzle:

    def __init__(self, wordlist_filename='../data/mit-wordlist.txt'):
        with open(wordlist_filename, 'r') as wordlist_file:
            self.wordlist_size = len([0 for _ in wordlist_file])
            wordlist_file.seek(random.randint(0, self.wordlist_size - 1))
            self.chosen_word = wordlist_file.readline(1)

    def get_word_line(self):
        pass

    def get_jumper(self):
        jumper = (" _____",
                  "/_____\\",
                  "\\     /",
                  " \\   /",
                  "   0",
                  "  /|\\",
                  "  / \\")
        return jumper

