class Parachuter():
    """A code template for an object representing an image.
    The responsibility of this class of objects is to display
    the image using ACII-art.
    
    Stereotype:
        Interfacer
    
    Attributes:
        self (Parachuter): An instance of the class of objects known as Console.
        self.ascii_art (list): A list with the images of the parachuter at different
                                stages.
    """

    def __init__(self):
        """The class constructor.
          
          Args:
              self (Parachuter): an instance of Parachuter.
        """
        self.ascii_art = [''' 
     ___
    /___\\
    \   /
     \ /
      0
     /|\ 
     / \\

   ^^^^^^^ ''', ''' 
    /___\\
    \   /
     \ /
      0
     /|\ 
     / \\

   ^^^^^^^ ''', '''
    \   /
     \ /
      0
     /|\ 
     / \\

   ^^^^^^^''', ''' 
     \ /
      0
     /|\ 
     / \\

   ^^^^^^^''', ''' 
      x
     /|\ 
     / \\

   ^^^^^^^''']