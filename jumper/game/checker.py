class Checker:
    """A code template for a checker. The
    responsibility of this class of objects is to receive a word-to-guess from the 
    game director, checks the guess from the jumper, and provide a hint for every 
    guess made by the jumper.

    Stereotype:
        Information Holder, Service Provider

    Attributes:
        word (string): The word that jumper should guess.
        hint (list): The list of character.
        correct (loolean): status of current guess
    """

    def __init__(self, word):
        """Class constructor. Declares and initializes instance attributes.

        Args:
          self (Checker): An instance of Checker.
          word (string): a new word
          """
        self.word = word.lower()
        self.hint = []
        for _ in self.word:
            self.hint.append("_")
        self.correct = True
        self.finished = False

    def checkAnswer(self, char):
        splitWord = self.Convert(self.word)

        if char in splitWord:
            self.correct = True

            for i in range(len(self.word)):
                if splitWord[i] == char:
                    self.hint[i] = char
        else:
            self.correct = False

        self.checkFinished()

    def checkFinished(self):
        if not "_" in self.hint:
            self.finished = True

    def isFinished(self):
        return self.finished

    def get_hint(self):
        return self.hint

    def isCorrect(self):
        return self.correct

    def Convert(self, string):
        list1 = []
        list1[:0] = string
        return list1