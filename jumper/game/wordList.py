class WordList:
    def __init__(self):
        # Opening a text doc to pull in words to use for the game
        with open('words.txt') as f:
            self.words = f.readlines()
