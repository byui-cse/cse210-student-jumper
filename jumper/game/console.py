import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.
        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

        
    def display_output(self, word_list):
        """Displays the given text on the screen. 
        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(word_list)

 