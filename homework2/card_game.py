import random


class CardGame:
    cards_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    list_of_card_dict_keys = list(cards_dict.keys())

    def __init__(self):
        self.first_card = random.choice(self.list_of_card_dict_keys)
        self.second_card = random.choice(self.list_of_card_dict_keys)

    def compare_two_cards(self):
        if self.cards_dict[self.first_card] > self.cards_dict[self.second_card]:
            print(self.first_card, 'won the', self.second_card)
        elif self.cards_dict[self.first_card] < self.cards_dict[self.second_card]:
            print(self.second_card, 'won the', self.first_card)
        else:
            print('A draw')


game1 = CardGame()
game1.compare_two_cards()

game2 = CardGame()
game2.compare_two_cards()

