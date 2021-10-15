import random
import glob
import os

"Creating a class to obtain and return the secret word from the text file"

class SecretWord:
    def get_word():
        os.chdir(r'cse210-student-jumper')
        myFiles = glob.glob('*.txt')
        os.chdir(r'jumper')
        myFiles2 = glob.glob('*.txt')
        os.chdir(r'game')
        myFiles3 = glob.glob('*.txt')

        index = random.randint(0,844)
        file = open('words.txt', 'r')
        l = file.readlines()
        selected_word = l[index].strip('\n')
        return selected_word
