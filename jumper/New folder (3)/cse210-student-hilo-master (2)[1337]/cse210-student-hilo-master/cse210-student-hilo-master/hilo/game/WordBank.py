import random
class word_bank:
    
    def get_word():
        word_list = ['buddy','bro','apple','bannana','orange','passionfruit','osteoperosis', 'supercalafragalisticexpialadocious']
        return(word_list[random.randint(0, len(word_list) - 1)])