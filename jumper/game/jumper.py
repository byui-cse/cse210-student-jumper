

class Jumper:
    """A code template for an object representing an immage.
    display image  using ACII-art. (I don't know what ACII-art is, I looked it up and it 
    doesn't make me understand what it is.)

     Stereotype: interfacer (don't know what this is either)

     Attributes self (Jumper): an instance of the class Console (my console class doesn't have a Jumper in it. )

     self.ascii_art (list) a list with the images of the parachuter at different stages. (I originally wrote this as a list of 
     seperate pieces that make up the whole, but this picture looks better than the one I did. )

    """

    def __init__(self):
        """ the class constructor.
         
         Args: self (Jumper): an instance of Jumper
        """
        self.ascii_art = ['''
         __
        /__\\
        \   /
         \ /
          0
         /|\
         /\\    

    ^^^^^^^^^^^ ''', '''
         __
        /__\\
        \  /
         \/
          0
        / | \
          /\  
     
     ^^^^^^^^^^^ ''', '''
        /__\\
        \   /
         \ /
          0
         /|\
         /\  
         
    ^^^^^^^^^^^^^  ''', '''
         \  /
          \/ 
           0
          /|\
           /\\
    
    ^^^^^^^^^^^^^  ''', '''
    
           \/
            0
           /|\\
           /\\   

    ^^^^^^^^^^^^^^  ''', '''
            X
           /|\\
            /\\   
            
    ^^^^^^^^^^^^^^^ ''']      
