import random
from urllib.request import urlopen
import re

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
    def __init__(self):

                
                self.guess_char = []
                self.tries = 0
                self.guess = ''
                self.selected_word = ''
                self.remaining_char = None
                
            


    def get_letter(self):
            
            guess = input('Guess letter [a-z]: ')
            self.guess = guess
            self.guess_char.append(guess)

         # this function checks if the letter put by the user is correct or false. If correct, he will continue playing, 
            # and if incorrect, he will lose a part of a parachute.
    def check_attempt(self):
               
            if self.guess in self.selected_word:  
                print()
            else: 
                self.tries += 1
        

# this function verifies or checks if the letter is in the selected word and then returns the letter and 
# the remaining dashes. 
    def verify_guess(self, guess):
           
        x = re.finditer(f'[{guess}]+', self.selected_word)
        match = [match.start() for match in x]

        for i in match:
            self.remaining_char[i] = f'{guess}'

        
        #The following is the easiest way to use verify-guess function in place of the above.
        """
        for letter in self.selected_word:
                if letter in self.guess:
                    print({letter}, end="")
                else:
                    print("_ ", end=""
        """