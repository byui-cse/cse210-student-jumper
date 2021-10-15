from wordProcessor import WordProcessor


class Jumper:
    def __init__(self):
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


    


jumper = Jumper()

jumper.printJumper()