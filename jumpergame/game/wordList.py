class WordList:
    """Code to create a word list that can be used by the game.


    Attributes: 
    self.words: a list of words to be used.

    Args:
    words: the word file to be used
    """
    def __init__(self, words):
        # Opening a text doc to pull in words to use for the game
        self.words = []
        with open('words.txt', 'r') as f:
            
            for line in f:
                self.words.append(line.strip())

