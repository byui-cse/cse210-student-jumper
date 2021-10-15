class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
    prompt (string): receive from the user a input. 
    text (string): output the input the user's imput
       
    """

    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Console): An instance of Console.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(text)