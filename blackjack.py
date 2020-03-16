import random
import functools

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
    curr_player_turn = None
    round_number = 0
    # @todo add betting?

    def __init__(self, player_name):
        print(LOGGING_NAME + "NEW GAME STARTED!")
        self.players = [Player(player_name)] # @TODO for now, just 1v1 the cpu
        self.players.append(Player("CPU"))
        self.deck = Deck() # assume its generated properly

        # deal every player 2 cards
        for player in self.players:
            player.hand = self.deck.draw(2)
        
        self.curr_player_turn = self.players[0]
        self.round_number += 1

    def hit(self, player_name):
        pass

    def stay(self, player_name):
        pass

    def calculate_winner(self):
        pass

    def calculate_bust(self):
        pass

    '''
    Returns a human-readable string (to be logged by caller, usually) about the state of the game.
    '''
    def game_state_log(self):
        # (PlayerName, Score, Hand?)
        log = "------------\n"
        log += LOGGING_NAME + LOG_GAME +  "Game State\n"
        log += "Round " + str(self.round_number) + "\n"
        log += "It is " + self.curr_player_turn.name + "\'s turn\n"
        for player in self.players:
            log += "\t > (" + player.name + ", " + str(player.calculate_score()) + ", " + player.log_player_hand()+ ")"
            log += '\n'
        log += "------------"
        return log

class Player():
    name = ""
    hand = []
    score = 0

    def __init__(self, name):
        self.name = name
        self.score = 0

    '''
    Calculate the current value of player's hand, and store it in a vArIaBlE (todo remove state...)
    '''
    def calculate_score(self):
        self.score = functools.reduce((lambda card1, card2: card1.value + card2.value), self.hand) 
        return self.score

    def log_player_hand(self):
        return str([str(card) for card in self.hand])

class Card():
    suit = None
    numerical_value = None 
    name = None
    color = None

    def __init__(self, name, suit, value):
        self.value = value
        self.name = name
        self.suit = suit

    def __str__(self):
        return str(self.name) + " of " + str(self.suit)

class Deck():
    deck = []

    def __init__(self):
        # @todo generate deck lmoa
        self.deck = [Card("Jack", "Clubs", 10),
                    Card("King", "Clubs", 10),
                    Card("Queen", "Clubs", 10),
                    Card("Ace", "Clubs", 1),
                    Card("Seven", "Clubs", 7),
                    Card("Six", "Clubs", 6),
                    Card("Five", "Clubs", 5),
                    Card("Four", "Clubs", 4),
                    Card("Three", "Clubs", 3),
                    Card("Two", "Clubs", 2),]
    

    def draw(self, num_cards):
        cards_drawn = []
        print("\n")
        print(LOGGING_NAME + LOG_DEBUG + "Deck before drawing: " + str(self))
        if len(self.deck) == 0:
            print(LOGGING_NAME + LOG_ERR + "@todo empty deck")
            return None
        while len(cards_drawn) < num_cards:
            card = self.deck.pop(random.randrange(len(self.deck)))
            cards_drawn.append(card)
        print(LOGGING_NAME + LOG_DEBUG + "Drew these cards: " + str([str(card) for card in cards_drawn]))
        print(LOGGING_NAME + LOG_DEBUG + "Deck after drawing: " + str(self))
        print("\n")

        return cards_drawn

    def shuffle(self):
        pass

    def __str__(self):
        return str([str(card) for card in self.deck])
