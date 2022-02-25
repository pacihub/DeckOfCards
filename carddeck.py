import random

class Deck:
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["C", "D", "H", "S"]


    def __init__(self):
        self.cards = []


    def fill_deck(self):
        for i in Deck.card_values:
            for j in Deck.suits:
                card = i + j
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []
        for i in range(n):
            if len(self.cards) == 0:
                break
            bingo = self.cards.pop()
            dealt_cards.append(bingo)

        return dealt_cards

    def sort(self):
        cards_by_suit = {'C' : [], 'D': [], 'H' : [], 'S': []}
        for i in self.cards:
            suit = i[-1]
            cards_by_suit[i[-1]].append(i)

        self.cards = []
        for j in cards_by_suit.values():
            for k in j:
                self.cards.append(k)

    def contains(self, card):
        if card in self.cards:
            return True
        else:
            return False

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck


    def get_cards(self):
        new_cards = self.cards[:]
        return new_cards

    def __len__(self):
        return len(self.cards)
