import pandas
from random import randint
import os


read = pandas.read_excel(os.getcwd() + '\\word.xlsx')
words = [i for i in read[0]]

past_word = []

class pick():
    def __init__(self, word_list):
        self.word_list = word_list
        
    def start(self):
        num = randint(0, len(self.word_list) - 1)
        past_word.append(self.word_list[num])
        self.word_list.remove(self.word_list[num])
        return self.word_list[num]

    def pick_word(self, player_word):
        for i in self.word_list:
            if i == player_word:
                self.word_list.remove(player_word)

        result =[]
        for i in self.word_list:
            if i.startswith(player_word[len(player_word) - 1]):
                result.append(i)
    
        result.sort(key=lambda item: (len(item), item), reverse=True)
        word = result[0]
        past_word.append(word)
        self.word_list.remove(word)
        return word
        

pick = pick(words)
bot_word = pick.start()
print(bot_word)


while True:
    player_word = input('단어 입력 : ')
    a = [i for i in past_word if i == player_word]
    if a != []:
        print('Retry')
    elif len(player_word) < 2:
        print('Retry')
    elif not bot_word[len(bot_word) - 1] == player_word[0]:
        print('Retry')
    else:
        try:
            bot_word = pick.pick_word(player_word)
        except IndexError:
            print('you win!!')
            exit()
        past_word.append(player_word)
        print(bot_word)

    a = []

