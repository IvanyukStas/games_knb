import random


class Games:

    def __init__(self, score=0):
        self.score = score

    def set_score(self):
        self.score += 1


class Knb(Games):

    def result_score(self):
        print(self.score)

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
        if player1 == '1' and player2 == '2':
            return True
        elif player1 == '2' and player2 == '3':
            return True
        elif player1 == '3' and player2 == '2' or '4':
            return True
        elif player1 == '4' and player2 == '1' or '2':
            return True
        else:
            return False

    def bot_get_choice(self):
        bot_choice = random.randint(1, 4)
        return bot_choice


if __name__ == '__main__':
    while True:
        games_knb = Knb()
        player1 = input('выберите 1-камень 3 ножницы 3 бумага 4 колодец: ')
        player2 = games_knb.bot_get_choice()
        if games_knb.get_choice(player1, player2) == True:
            games_knb.set_score()
            print(player2)
        print(games_knb.score)