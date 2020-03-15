# hello world
import os
import sys
import discord
from dotenv import load_dotenv
from blackjack import Blackjack

LOGGING_NAME = "[Discord-Card-Bot] "
LOG_ERR = "(ERROR) "
LOG_DEBUG = "(DEBUG) "

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
            else:
                print(LOGGING_NAME + LOG_ERR + player + "is already in game!")

        # figure out how to do repl loop
        if message.content == "--blackjack hit":
            if player in self.player_game_dict.keys():
                curr_game = self.player_game_dict[player]
            else:
                print('bitch')
        elif message.content == "--blackjack stay":
            print("stay horsey")
        elif message.content == "--blackjack quit":
            print("haha loser")
                

        # if message
    def find_game(self, player_name):
        # iterate through curr_games until u find player
        # @todo one player in multiple games?
        pass

client = CardGameClient()
client.run(TOKEN)


# start off with solo blackjack vs bot