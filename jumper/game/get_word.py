import random
import glob
import os

class SecretWord:
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

    print(selected_word)