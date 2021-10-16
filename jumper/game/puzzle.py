import random

class Puzzle:
    """ Template for the secret word. The computer choses this word from our list of words,
    This class is responsible for getting a word for the player to guess.
    
    stereotype: Info Holder

    Attributes: picked_word (string) this is the word from the list
                word (list) this is a list of words to use
                word_choice (list)  choices from the user


    """

    def __init__(self):
        """ class constructor
        Args : self (Puzzle) an instance of Puzzle
        
        """
        

        word =["happy", "silly", "sleepy", "hungry","branch", "status","commit"]
        chosen_word = [] # i think i need each letter to be it's own string. 

        self.word = word.random.choice(word) #im not sure this will work it looks wrong. it's supposed to chose a word from the list
        self.chosen_word = self.word.append()#take word chosen from word list and put it into it's own list.
        self.chosen_word_letters = ["_"] * len(self.chosen_word) #  I want  this to make each letter into a string.
        




    def player_chose_letter(self):

        guess = input("guess a letter [a-z] : ")


        pass

    def guess_end(self):
        """ return True if the right word is guessed. Return False if not. 
        
        Args: self (Puzzle) an instance of Puzzle
        """

        if "_" not in self.chosen_word:
            return True
        else: 
            return False

    def show_letters(self):
        """ Returns two strings: one with right guesses, one with wrong guesses ( I got this from RealThadeus, 
        I couldn't figure it out on my own. feel free to change it.)
        
        Args: self(Puzzle): an instance of Puzzle


        """
        w_chart = ""
        for element in self.chosen_word_letters:
            w_chart += element + ""

        w_letters = ""
        if len(self.wrong_letters) > 0:
            for element in self.chosen_word_letters:
                w_letters += "" + element
        return w_chart, w_letters            

