import pandas as pd
from pandas import DataFrame
from random import randint
import os

path = os.path.join(os.getcwd() + "\\"  + "data.xlsx")
print(path)
words = pd.read_excel(path)

words = words['kword']
word_result = [i for i in words]

class pick_word():
    def __init__(self, words):
        self.word_list = words
    
    def pick(self, player_word):

        kword_list = []
        last_word = player_word[len(player_word) - 1]

        kword_list = [i for i in self.word_list if i[0] in last_word]

        num = randint(0, len(kword_list))

        return kword_list[num]

    def add(self, player_word):
        word_result.append(player_word)
                

bot = pick_word(words)

while True:
    player_word = input('단어 입력 : ')

    for i in words:
        if not(i == player_word):
            bot.add(player_word)
            df = DataFrame({"kword": word_result}, index=None)
            writer = pd.ExcelWriter('data.xlsx')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.close()
            break

    try:
        bot_word = bot.pick(player_word)
    except IndexError:
        print('you win!!')
        quit()
    
    print(bot_word)