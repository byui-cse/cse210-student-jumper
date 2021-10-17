class parachuter:
    """Code to represent the jumper image.

    Stereotype:
        Information holder

    Attributes:
        the_parachuter(list): hold the list with the string objects for the jumper image
        tricts(integer): counter to be able to print 3 strings at a time
        tries(integer): counter for the number of tries 
    """
    def __init__(self):
        """Class constructor, Declares and initializes instance attributes.
        
        Args:
            self (Parachuter): An instance of Parachuter
        """
        self.the_parachuter = [
            ' ','___',' ',
            '/','___','\\',
            '\\','   ','/',
            '','\\   /',' ',
            ' ',' 0 ',' ',
            ' /','|','\\',
            ' /',' ','\\'
        ]
        
        self.ticks = 0

        self.tries = 0
        
    
    def print_parachuter(self):
        """Prints the image of the jumper

        Args:
            self (Parachuter): An isntance of Parachuter
        
        Returns:
            list that is printed in 3x5 order
        """
        for i in self.the_parachuter:
            print(f'{self.the_parachuter[self.ticks]} {self.the_parachuter[self.ticks+1]} {self.the_image[self.ticks+2]}')
            self.ticks += 3

    def update_parachuter(self):
        """Keeps track of the number of tries the player has failed 
        and updates the list to cut the parachute.

        Args:
            self (Parachuter): An isntance of Parachuter

        Returns:
            an instance of self.print_parachute to the director
        """
    
        self.tries += 1

        if self.tries == 1:
            self.the_parachuter[1] = ' '
        elif self.tries == 2:
            self.the_parachuter[3] = ' '
            self.the_parachuter[4] = ' '
            self.the_parachuter[5] = ' '
        elif self.tries == 3:
            self.the_parachuter[6] = ' '
            self.the_parachuter[8] = ' '
        elif self.tries == 4:
            self.the_parachuter[10] = '  '
            self.the_parachuter[13] = 'x'

        return self.print_parachuter()