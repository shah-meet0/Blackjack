from cards import Deck


class BlackjackGame:

    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []

    def run(self):
        game_running = True
        while game_running:
            action = input("What would you like to do? (Start, Quit)\n").lower()
            if action == "start":
                self.game()
            elif action == "quit":
                print("Thanks for playing")
                game_running = False
            else:
                print("Invalid Input")

    def game(self):
        deck = Deck()
        game_over = False
        while not game_over:
            deck.shuffle()
            self.player_cards.append(deck.draw())
            self.dealer_cards.append(deck.draw())
            do_dealer_turn = self.player_turn(deck)
            if do_dealer_turn:
                self.dealer_turn(deck)
            deck.recombine()
            print(self.winner_statement(self.decide_winner()))
            self.player_cards.clear()
            self.dealer_cards.clear()
            game_over = True

    def player_turn(self, deck):
        while self.get_player_value() < 21:
            print(self.describe())
            action = self.get_hit_stand()
            if action == "hit":
                self.player_cards.append(deck.draw())
            else:
                return True
        if self.get_player_value() == 21:
            print(self.describe())
            return True
        else:
            print(self.describe())
            return False

    def dealer_turn(self, deck):
        self.dealer_cards.append(deck.draw())
        print(self.describe())
        while self.get_player_value(True) < 17:
            self.dealer_cards.append(deck.draw())
            print(self.describe())
        print(self.describe())

    def decide_winner(self):
        player_value = self.get_player_value()
        dealer_value = self.get_player_value(True)
        if player_value > 21:
            return "dealer"
        elif dealer_value > 21:
            return "player"
        elif player_value == dealer_value:
            return "tie"
        elif player_value > dealer_value:
            return "player"
        else:
            return "dealer"

    def winner_statement(self, winner):
        if winner == "player":
            return "Congrats, you won."
        if winner == "dealer":
            return "Sorry, you lost."
        if winner == "tie":
            return "Game was tied."

    def get_player_value(self, dealer=False):
        value = 0
        number_aces = 0
        if dealer:
            for card in self.dealer_cards:
                value += card.get_value()
        else:
            for card in self.player_cards:
                if card.card_name == "Ace":
                    number_aces += 1
                value += card.get_value()
            while number_aces > 0 and value > 21:
                value = value - 10
                number_aces = number_aces - 1
        return value

    def describe(self):
        dealer_value = self.get_player_value(True)
        your_value = self.get_player_value(False)
        string = "Your cards:\n"
        for card in self.player_cards:
            string += str(card) + "\n"
        string += "Value: " + str(your_value) + "\n"
        string += "Dealer cards:\n"
        for card in self.dealer_cards:
            string += str(card) + "\n"
        string += "Value: " + str(dealer_value)+"\n"
        string += "--------------------------------------------"
        return string

    @staticmethod
    def get_hit_stand():
        action = input("Hit or Stand?\n").lower()
        if action == "hit" or action == "stand":
            return action
        else:
            print("Invalid Input")
            return BlackjackGame.get_hit_stand()

    @staticmethod
    def get_continue_quit():
        action = input("Hit or Stand?\n").lower()
        if action == "continue" or action == "quit":
            return action
        else:
            print("Invalid Input")
            return BlackjackGame.get_continue_quit()