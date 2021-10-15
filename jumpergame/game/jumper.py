from game.wordProcessor import WordProcessor


class Jumper:
    """A class dedicated to printing the jumper and keeping track of points."""
    def __init__(self):
        self.keepPlaying = True
        self.wrongGuess = 0
        self.processor = WordProcessor()
        self.asciiArt = []
        self.asciiArt.append('  ___ ')
        self.asciiArt.append(" /___\\")
        self.asciiArt.append(' \\   /')
        self.asciiArt.append('  \\ /')
        self.asciiArt.append('   0   ')
        self.asciiArt.append('  /|\\  ')
        self.asciiArt.append('  / \\  ')
        self.asciiArt.append('\n^^^^^^^')
        

    def printJumper(self):
        for line in self.asciiArt:
            print(line)

    def checkCorrect(self, letter):
        if (not self.processor.checkLetter(letter)):
            self.wrongGuess += 1
            self.asciiArt.remove(0)
    
    def continuePlay(self, letter):
        if letter == '  0  ':
            self.asciiArt[0] = '  X  '
            self.keepPlaying = False


    


jumper = Jumper()

jumper.printJumper()