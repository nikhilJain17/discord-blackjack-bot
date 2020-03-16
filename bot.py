# hello world
import os
import sys
import discord
from dotenv import load_dotenv
from blackjack import Blackjack

LOGGING_NAME = "[Discord-Card-Bot] "
LOG_ERR = "(ERROR) "
LOG_DEBUG = "(DEBUG) "
LOG_GAME = "(Game) "


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv("DISCORD_SERVER")

if TOKEN == None:
    sys.exit(LOGGING_NAME + LOG_ERR + "Couldn't load discord token from .env file.")

class CardGameClient(discord.Client):

    game_stats = [] # nice feat...keep track of who is winning and losing :3
    current_games = []
    player_game_dict = {}

    async def on_ready(self):
        print(LOGGING_NAME + LOG_DEBUG + str(client.user) + " has connected to the server " + str(client.guilds[0].name ))

    # this is like the repl loop
    async def on_message(self, message):
        print(LOGGING_NAME + LOG_DEBUG + "message from {0.author}: {0.content}".format(message))
        print(message)
        print(message.author)
        print(message.channel)
        print(message.content)

        player = str(message.author)

        # start a game...in a new thread???
        if (message.content == "--blackjack start"):
            if player not in self.player_game_dict.keys():
            # init a game
                new_game = Blackjack(player)
                self.current_games.append(new_game)
                self.player_game_dict[player] = new_game
                print(new_game.game_state_log())

                # need to display one of dealer's cards face up 

                # calculate winner at end of each round
                # in this case, since its first round, it's if anyone has a natural

            else:
                print(LOGGING_NAME + LOG_ERR + player + " is already in game!")

        # @todo figure out how to do repl loop here
        if message.content == "--blackjack hit":
            if player in self.player_game_dict.keys():
                curr_game = self.player_game_dict[player]
            else:
                print(LOGGING_NAME + LOG_ERR + player + " is not in a game!")
        elif message.content == "--blackjack stay":
            # if the player stays, then the dealer plays
            # @todo dealer logic here
            print("stay horsey")
            await message.channel.send(player + " chose to stay. Dealer's turn!")
            if player in self.player_game_dict.keys():
                curr_game = self.player_game_dict[player]
                print(LOGGING_NAME + LOG_GAME + player + " has chosen to stay. Dealer's turn!")
                curr_game.curr_player_turn = curr_game.players[1] # set it to CPU's turn (@todo need a better way than just 2 elem array of players lol)
                print(curr_game.game_state_log())

            else:
                print(LOGGING_NAME + LOG_ERR + player + " is not in a game!")

            
            # Dealer Gameplay:
            # dealer_total >= 17, stand
            # dealer_total <= 16, hit
            # if dealer has ace and ace as 11 would bring total >= 17, stay


        elif message.content == "--blackjack quit":
            print("haha loser")
        elif message.content == "--blackjack help":
            print("This is a help message")
                

        # if message
    def find_game(self, player_name):
        # iterate through curr_games until u find player
        # @todo one player in multiple games?
        pass

client = CardGameClient()
client.run(TOKEN)


# start off with solo blackjack vs bot