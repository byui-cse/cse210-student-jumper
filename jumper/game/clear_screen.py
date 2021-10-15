import platform
import os


class ClearScreen():
    """A code template for an object which interacts with the display.
    The responsibility of this class of objects is to determine the 
    type of OS and clear the screen accordingly.
    
    Stereotype:
        Interfacer
    
    Attributes:
        self.system (string): A string containing the OS.
        self.clear (string):  A string with the command to clear the screen.
    """

    def __init__(self) -> None:
        """The class constructor.
        
        Args:
            self (ClearScreen): an instance of ClearScreen.
        """
        self.system = platform.system()
        self.clear = ""

    def clear_screen(self):
        """Clears the screen with the right command depending
        on the OS.
        
        Args:
            self (ClearScreen): an instance of ClearScreen.
        """
        #if Windows:
        if self.system == 'Windows':
            self.clear = lambda: os.system("cls")
        #if Linux:
        else:
            self.clear = lambda: os.system("clear")

        self.clear