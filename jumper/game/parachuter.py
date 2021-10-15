class parachuter:

    def __init__(self):
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
        
        for i in self.the_image:
            print(f'{self.the_image[self.ticks]} {self.the_image[self.ticks+1]} {self.the_image[self.ticks+2]}')
            self.ticks += 3

    def update_parachuter(self):
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

        return self.the_parachuter