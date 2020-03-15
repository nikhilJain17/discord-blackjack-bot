import random

LOGGING_NAME = "[Blackjack] "
LOG_ERR = "(ERROR) "
LOG_DEBUG = "(DEBUG) "
LOG_GAME = "(Game) "

class Blackjack():
    game_id = None
    players = []
    deck = []
    dealer_hand = []
    game_over = False
    winner = None

    def __init__(self, player_name):
        print(LOGGING_NAME + "NEW GAME STARTED!")
        self.players = [Player(player_name)] # @TODO for now, just 1v1 the cpu
        self.players.append(Player("CPU"))
        self.deck = Deck() # assume its generated properly

        # deal every player 2 cards
        for player in self.players:
            player.hand = self.deck.draw(2)
            print(LOGGING_NAME + LOG_GAME + str(player.name) + " holding " + str(player.hand))
        
    def hit(self, player_name):
        pass

    def stay(self, player_name):
        pass

    def calculate_winner(self):
        pass

class Player():
    name = ""
    hand = []

    def __init__(self, name):
        self.name = name

class Card():
    suit = ""
    value = ""
    color = ""

    def __init__(self, suit, value, color):
        self.suit = suit
        self.value = value
        self.color = color

    def __str__(self):
        print(str(self.value) + " of " + str(self.suit))

class Deck():
    deck = []

    def __init__(self):
        # @todo generate deck lmoa
        self.deck = ["1", "2", "3", "4", "5", "6", "7", "8"]
    

    def draw(self, num_cards):
        cards_drawn = []
        print(LOGGING_NAME + LOG_DEBUG + "deck before drawing: " + str(self.deck))
        if len(self.deck) == 0:
            print(LOGGING_NAME + LOG_ERR + "@todo empty deck")
            return None
        while len(cards_drawn) < num_cards:
            card = self.deck.pop(random.randrange(len(self.deck)))
            cards_drawn.append(card)
        print(LOGGING_NAME + LOG_DEBUG + "drew these cards: " + str(cards_drawn))
        print(LOGGING_NAME + LOG_DEBUG + "deck after drawing: " + str(self.deck))

        return cards_drawn

    def shuffle(self):
        pass

    def __str__(self):
        print(self.deck)
