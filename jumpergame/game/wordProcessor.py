from game.wordList import WordList
import random

class WordProcessor:
    """A class to process words and check guesses."""
    def __init__(self):
        """Class constructor
        
        Wordlist: list of words to be chosen from
        letters: list of letters to be used in game
        wordspace: blank space to be used in letters not guessed yet
        """
        self.wordList = WordList('words.txt').words
        self.letters = list(self.wordList[random.randint(0, len(self.wordList) - 1)])
        self.wordSpace = []
        for l in self.letters:
            self.wordSpace.append(' _ ')

        

    def checkLetter(self, letter):
        """A method to check the letter and replace it if the guess is correct.
        
        Args:
            self(wordprocessor): An instance of the word processor class.
            letter: the letter guessed by the user
        """
        change = False
        for x in range(len(self.letters)):
            if self.letters[x] == letter:
                self.wordSpace[x] = f' {letter} '
                change = True
        return change

    def printWord(self):
        """A method to print the word cleanly.
        
        Args:
            self(WordProcessor): An instance of the word processor class.
        """
        print(''.join(self.wordSpace))

    def checkWin(self):
        """Method to check whether or not the player has won the game.
        Args: 
            self(WordProcessor): an instance of the word processor class.
        """
        win = True
        for l in self.letters:
            if l == ' _ ':
                win = False
        return win

    def get_letter(self):
        """A method for getting a guess from the user.
        
        Args:
            self(WordProcessor): an instance of the word processor class.
        """
        letter = input("Please guess a letter: ")
        return letter