from random import randint
import functools


def repeat_func(number_times):
    def repeater(func):
        @functools.wraps(func)
        def repeat_wrapper(*args, **kwargs):
            for i in range(number_times):
                func(*args, **kwargs)

        return repeat_wrapper

    return repeater


class Card:

    def __init__(self, trump, name):
        self.trump = trump
        self.card_name = name

    def __str__(self):
        return self.card_name + " of " + self.trump


class BlackjackCard(Card):

    def __init__(self, trump, name, value):
        super().__init__(trump, name)
        self.value = value

    def get_value(self):
        return self.value

class Deck:

    def __init__(self):
        trumps = ["Spades", "Hearts", "Clubs", "Diamonds"]
        cards = []
        value_dict = {"Ace": 11}
        for i in range(2, 11):
            value_dict[str(i)] = i
        value_dict["Jack"] = 10
        value_dict["Queen"] = 10
        value_dict["King"] = 10
        for card in value_dict.keys():
            for trump in trumps:
                cards.append(BlackjackCard(trump, card, value_dict[card]))
        self.cards = cards
        self.discard_pile = []

    def draw(self):
        card_drawn = self.cards.pop(0)
        self.discard_pile.append(card_drawn)
        return card_drawn

    @repeat_func(1000)
    def shuffle(self):
        index_one = randint(0, 51)
        index_two = randint(0, 51)
        self.cards.insert(index_two, self.cards.pop(index_one))

    def recombine(self):
        for i in range(0, len(self.discard_pile)):
            self.cards.insert(0, self.discard_pile.pop(0))

    def __str__(self):
        string = ""
        for card in self.cards:
            string = string + str(card) + "\n"
        return string

    def __len__(self):
        return len(self.cards)