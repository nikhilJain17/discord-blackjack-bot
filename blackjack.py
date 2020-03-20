import random
import functools

LOGGING_NAME = "[Blackjack] "
LOG_ERR = "(ERROR) "
LOG_DEBUG = "(DEBUG) "
LOG_GAME = "(Game) "

class Blackjack():
    game_id = None
    players = {}
    deck = []
    dealer_hand = []
    game_over = False
    winner = None
    curr_player_turn = None
    round_number = 0
    # @todo add betting?

    def __init__(self, player_name):
        print(LOGGING_NAME + "NEW GAME STARTED!")
        self.players[player_name] = Player(player_name) # @TODO for now, just 1v1 the cpu
        self.players["CPU"] = Player("CPU")
        self.deck = Deck() # assume its generated properly

        # @todo deal every player 2 cards
        # for player_key in self.players.keys():
        #     self.hit(player_key, 2)
        for player in self.players.values():
            player.hand = self.deck.draw(2)
        # map((lambda player_name : self.hit(player_name, 2)), self.players.keys())
        
        self.curr_player_turn = self.players[player_name]
        self.round_number += 1

    def hit(self, player_name, quantity):
        if player_name not in self.players.keys():
            print(LOGGING_NAME + LOG_ERR + " invalid player tried hitting: " + player_name)
            return None
        else:    
            player = self.players[player_name]
            new_card = self.deck.draw(quantity)
            player.hand += new_card
            player.calculate_score()
            # print(LOGGING_NAME, LOG_DEBUG, player_name, player.log_player_hand())
            print(LOGGING_NAME, LOG_DEBUG, self.game_state_log())
            return new_card
        
    def stay(self, player_name):
        pass

    def calculate_winner(self):
        pass

    def calculate_bust(self, player_name):
        return self.players[player_name].score > 21

    '''
    Returns a human-readable string (to be logged by caller) about the state of the game.
    '''
    def game_state_log(self):
        # (PlayerName, Score, Hand?)
        log = "------------\n"
        log += LOGGING_NAME + LOG_GAME +  "Game State\n"
        log += "Round " + str(self.round_number) + "\n"
        # log += "It is " + self.curr_player_turn.name + "\'s turn\n"
        for player in self.players.values():
            log += "\t > (" + player.name + ", " + str(player.calculate_score()) + ", " + player.log_player_hand()+ ")"
            log += '\n'
        log += "------------"
        return log

    '''
    Returns a human-readable string about the state of the game relative to a certain player
     (to be sent as discord message)
    '''
    def game_state_msg(self):
        msg = "------------\n"
        msg += "The Epic Showdown: " + functools.reduce((lambda n1, n2 : n1 + " vs " + n2), self.players.keys()) + " \n"
        msg += "Round " + str(self.round_number) + "\n"
        msg += "It is " + self.curr_player_turn.name + "\'s turn\n"
        for player in self.players.values():
            msg += "\t > (" + player.name + ", " + str(player.calculate_score()) + ", " + player.log_player_hand()+ ")"
            msg += '\n'
        msg += "------------"
        return msg
        

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
        print("concat", self.hand[0])
        # self.score = functools.reduce((lambda card1, card2: card1.value + card2.value), self.hand, 0) 
        self.score = sum([card.value for card in self.hand])
        return self.score

    def log_player_hand(self):
        return self.name + "'s current hand: " + functools.reduce((lambda x, y: x + "\n" + y), [str(card) for card in self.hand], "\n")

class Card():
    suit = None
    numerical_value = None 
    name = None
    color = None # @TODO delete field this probably

    def __init__(self, name, suit, value):
        self.value = value
        self.name = name
        self.suit = suit

    def __str__(self):
        return "<" + str(self.name) + " of " + str(self.suit) + "> "

    def img_filename(self):
        return "./card_assets/" + self.name[0] + self.suit[0] + ".jpg"
        

    

class Deck():
    deck = []

    def __init__(self):
        # generate deck lmoa
        self.deck = []
        for suit in ["Club", "Heart", "Spade", "Diamond"]:
            for name, value in [("King", 10),("Queen", 10), ("Jack", 10), ("10", 10), ("9", 9), 
            ("8", 8), ("7", 7), ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)]:
                self.deck.append(Card(name, suit, value))
        
        

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
        return functools.reduce((lambda x, y: x + ", " + y), [str(card) for card in self.deck])
