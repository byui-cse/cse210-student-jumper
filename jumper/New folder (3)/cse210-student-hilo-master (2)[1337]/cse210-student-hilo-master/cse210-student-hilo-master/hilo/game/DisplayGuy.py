from game.WordBank import word_bank

class board:
    def __init__(self) -> None:
        self.fails = 0
        self.blanks = []
        self.word = word_bank.get_word()
        i = 0
        while i < len(self.word):
            self.blanks.append('*')
            i += 1
    
    def guy(self):
            print(self.blanks)
    
    def parachute(self):
        if self.fails < 1:
            print( " ___")
        if self.fails < 2:
            print('/   \ ')
        if self.fails < 3:
            print('\___/')
            print(' \|/')
            print('  o')
            print(' /I\ ')
            print(' / \ ')
        else:
            print('  x')
            print(' /I\ ')
            print(' / \ ')
            print('You died')
    
    def check_guess(self, letter):
        is_here = False
        for i in range(len(self.word)):
            if letter == self.word[i]:
                self.blanks[i] = letter
                is_here = True
        if is_here != True:
            self.fails += 1

    def stayin_alive(self):
        if self.fails > 2:
            return False
        else:
            return True

    def check_win(self):
        if '*' not in self.blanks:
            return True
        else:
            return False
