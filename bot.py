# hello world
import os
import sys
import discord
from dotenv import load_dotenv
from blackjack import Blackjack
import time

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

        player_name = str(message.author)

        # start a game...in a new thread???
        if (message.content == "--blackjack start"):
            if player_name not in self.player_game_dict.keys():
            # init a game
                new_game = Blackjack(player_name)
                self.current_games.append(new_game)
                self.player_game_dict[player_name] = new_game
                print(new_game.game_state_log())
                await message.channel.send("New Game between " + player_name + " and CPU!!!")
                await message.channel.send(new_game.players[player_name].log_player_hand())
                await message.channel.send(player_name + "'s score: " + str(new_game.players[player_name].calculate_score()))

                # need to display one of dealer's cards face up 

                # calculate winner at end of each round
                # in this case, since its first round, it's if anyone has a natural

            else:
                print(LOGGING_NAME + LOG_ERR + player_name + " is already in game!")
                await message.channel.send(player_name + " is already in a game!!!")

        # @todo figure out how to do repl loop here
        if message.content == "--blackjack hit":
            # is it a valid game?
            if player_name in self.player_game_dict.keys():
                curr_game = self.player_game_dict[player_name]
                curr_player = curr_game.players[player_name]
                # draw a card
                new_card = curr_game.hit(player_name, 1)
                await message.channel.send(player_name + " drew " + new_card[0].__str__())
                await message.channel.send("After hitting, " + curr_player.log_player_hand())
                await message.channel.send(player_name + "'s score: " + str(curr_player.calculate_score()))
                if curr_game.calculate_bust(player_name):
                    await message.channel.send(player_name + " busted! haha loser")
                    # end the game by removing from dictionary :(
                    self.player_game_dict.pop(player_name)
                    # @todo have cpu play it out?
            else:
                await message.channel.send(player_name + " is not in a game! To play, use --blackjack start.")
                print(LOGGING_NAME + LOG_ERR + player_name + " is not in a game!")

        elif message.content == "--blackjack stay":
            # if the player stays, then the dealer plays
            # @todo dealer logic here
            print("stay horsey")
            if player_name in self.player_game_dict.keys():
                await message.channel.send(player_name + " chose to stay. Dealer's turn!")
                curr_game = self.player_game_dict[player_name]
                print(LOGGING_NAME + LOG_GAME + player_name + " has chosen to stay. Dealer's turn!")
                curr_game.curr_player_turn = curr_game.players["CPU"] # set it to CPU's turn (@todo need a better way than just 2 elem array of players lol)
                print(curr_game.game_state_log())

                # send cpu's hand
                curr_player = curr_game.players[player_name]
                cpu_player = curr_game.players["CPU"]
                await message.channel.send(cpu_player.log_player_hand())
                cpu_score = cpu_player.calculate_score()
                while cpu_player.calculate_score() < 17 :
                    curr_card = curr_game.hit("CPU", 1)[0]
                    cpu_score = cpu_player.calculate_score()
                    await message.channel.send("-----------\nCPU drew " + str(curr_card))
                    await message.channel.send(cpu_player.log_player_hand())
                    await message.channel.send("CPU score " + str(cpu_player.calculate_score()))
                if cpu_score > 21:
                    print(LOGGING_NAME, LOG_GAME, "cpu busted")
                    await message.channel.send("CPU busted. You win!!!")
                elif cpu_score < curr_player.calculate_score():
                    print(LOGGING_NAME, LOG_GAME, "cpu lost")
                    await message.channel.send("CPU lost. You win!!!")
                elif cpu_score > curr_player.calculate_score():
                    print(LOGGING_NAME, LOG_GAME, "cpu won")
                    await message.channel.send("CPU won. You lose :( F")
                elif cpu_score == curr_player.calculate_score():
                    print(LOGGING_NAME, LOG_GAME, "tie")
                    await message.channel.send("It's a tie...")

                self.player_game_dict.pop(player_name)





            else:
                await message.channel.send(player_name + " is not in a game!")
                print(LOGGING_NAME + LOG_ERR + player_name + " is not in a game!")

            
            # Dealer Gameplay:
            # dealer_total >= 17, stand
            # dealer_total <= 16, hit
            # if dealer has ace and ace as 11 would bring total >= 17, stay


        elif message.content == "--blackjack quit":
            print("haha loser")
        elif message.content == "--blackjack help":
            print("This is a help message")
        elif message.content == "--blackjack 69420":
            time.sleep(1)
            await message.channel.send("--blackjack 69420")
                

        # if message
    def find_game(self, player_name):
        # iterate through curr_games until u find player
        # @todo one player in multiple games?
        pass

client = CardGameClient()
client.run(TOKEN)


# start off with solo blackjack vs bot