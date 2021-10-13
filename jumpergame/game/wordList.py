class WordList:
    def __init__(self, words):
        # Opening a text doc to pull in words to use for the game
        self.words = []
        with open('words.txt', 'r') as f:
            
            for line in f:
                self.words.append(line.strip())

