import random
import linecache

class Puzzle:

    def __init__(self, wordlist='../data/mit-wordlist.txt', min_chars=2):
        self.wordlist = wordlist
        self.min_word_chars = min_chars

        with open(wordlist, 'r') as wordlist_file:
            self.wordlist_size = len([0 for _ in wordlist_file])
        
        self.previously_done = []
        self.choose_new_word()

    
    def choose_new_word(self):
        self.chosen_word = ''
        while (len(self.chosen_word) < self.min_word_chars) and (self.chosen_word not in self.previously_done):
            self.chosen_word = linecache.getline(self.wordlist, random.randint(0, self.wordlist_size - 1)).strip()
        self.previously_done.append(self.chosen_word)

    def get_word_line(self):
        pass


class Jumper:

    def __init__(self, num_lives=3):
        if num_lives < 3:
            raise(ValueError('Jumper cannot have less than 3 lives.'))
        self.num_lives = num_lives
        self.max_para = 2 * num_lives - 3
        self.build_jumper()

    def build_jumper(self):
        jumpman = []
        jumpman.append(' ' + '_' * self.max_para)
        jumpman.append('/' + '_' * self.max_para +'\\')
        for spaces in range(self.max_para, 1, -2):
            align = calc_alignment(self.max_para, spaces)
            jumpman.append(align + '\\' + ' ' * spaces + '/')
        
        jumpman.append(calc_alignment(self.max_para, -1) + '0')
        jumpman.append(calc_alignment(self.max_para, 1) + '/|\\')
        jumpman.append(calc_alignment(self.max_para, 1) + '/ \\')
        self.jumpman = tuple(jumpman)
    
    def print_jumper(self):
        # TODO: change to reflect lost lives
        for line in self.jumpman:
            print(line)
    
    def lose_life(self):

        def remove_top_layer(line):
            if line == self.jumpman[0]:
                return False
            return True
        
        def change_head(line):
            if line[-1] == '0':
                return line[:-1] + 'X'
            return line

        self.num_lives -= 1
        self.jumpman = tuple(filter(remove_top_layer, self.jumpman))
        if self.num_lives == 0:
            self.jumpman = tuple(map(change_head, self.jumpman))
        return self.num_lives


def calc_alignment(total_space, used_space, char=' '):
    num_align = (total_space - used_space) / 2
    return char * int(num_align)
