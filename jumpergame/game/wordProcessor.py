from game.wordList import WordList
import random

class WordProcessor:
    def __init__(self):
        self.wordList = WordList('words.txt').words
        self.letters = list(self.wordList[random.randint(0, len(self.wordList) - 1)])
        self.wordSpace = []
        for l in self.letters:
            self.wordSpace.append(' _ ')

        

    def checkLetter(self, letter):
        change = False
        for x in range(len(self.letters)):
            if self.letters[x] == letter:
                self.wordSpace[x] = f' {letter} '
                change = True
        return change

    def printWord(self):
        print(''.join(self.wordSpace))

    def checkWin(self):
        win = True
        for l in self.letters:
            if l == ' _ ':
                win = False
        return win
