import os
import random
from colorama import Fore, Style


class Games:
    '''Основной класс'''


    def __init__(self, score_player1=0, score_player2=0):
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def set_score_player1(self):
        self.score_player1 += 1

    def set_score_player2(self):
        self.score_player2 +=1

class Knb(Games):
    '''Игра камень ножницы бумага'''


    def get_choice(self, player1, player2) -> bool:
        '''
        1-kamen
        2-noshici
        3-бумага
        4-колодец
        :param player1:
        :param player2:
        :return:
        '''
        if player1 == '1' and player2 == 2:
            return True
        elif player1 == '2' and player2 == 3:
            return True
        elif player1 == '3' and (player2 == 2 or player2 == 4):
            return True
        elif player1 == '4' and (player2 == 1 or player2 == 2):
            return True
        else:
            return False

    def bot_get_choice(self):
        bot_choice = random.randint(1, 4)
        return bot_choice



if __name__ == '__main__':
    games = {
        '1': 'КАМЕНЬ',
        '2': 'НОЖНИЦЫ',
        '3': 'БУМАГА',
        '4': 'КОЛОДЕЦ'
    }
    games_knb = Knb()
    player1 = ''
    while not player1 == 'q':
        player1 = input('выберите 1-камень 2-ножницы 3-бумага 4-3колодец: ')
        if player1 not in ['1', '2', '3', '4']:
            continue
        player2 = games_knb.bot_get_choice()
        if games_knb.get_choice(player1, player2) == True:
            games_knb.set_score_player1()
            print(Fore.RED + f'Твой выбор {games[player1]}, БОТ ответил {games[str(player2)]}!')
            print('Это твоя ', games_knb.score_player1, 'победа!')
        elif player1 == str(player2):
            print(Fore.BLUE + 'НИЧЬЯ')
        else:
            games_knb.set_score_player2()
            print(Fore.YELLOW + f'Твой выбор {games[player1]}, БОТ ответил {games[str(player2)]}!')
            print(f'Бот выиграл {games_knb.score_player2} раз!')
        print(Style.RESET_ALL)
        print(f'СЧЕТ {games_knb.score_player1}:{games_knb.score_player2}')
    print('Good Bye My Love')


