import random
colors = ["\033[1;32;1mGreen\033[m","\033[1;34;1mBlue\033[m","\033[1;31;1mRed\033[m","\033[1;33;1mYellow\033[m"]
nums = range(10)
deck = []
shuffled = []
played_cards = []
player, bot_2, bot_3, bot_4 = [], [], [], []


# Creating our cards
class UnoCard:
    def __init__(self, color, num):
        self.c = color
        self.n = num

    def __str__(self):
        return str(str(self.c) + " " + str(self.n))


    def CanPlay(self,other):
        if (self.c == other.c) or (self.n == other.n):
            return True
        else:
            return False


def Cut(list_r,list_a,a):
    list_r.remove(a)
    list_a.append(a)


def CheckDeck(deck,played_cards):
    if len(deck) <= 4:
        random.shuffle(played_cards)
        deck.extend(played_cards)

def CheckWinner():
    if len(player) == 0:
        print("\n\033[1;32;1mCongratulations. You Won.\033[m")
        quit()
    if len(bot_2) == 0:
        print("\n\033[1;31;1mGame Over.\033[m AI1 \033[1;32;1mWins.\033[m")
        quit()
    if len(bot_3) == 0:
        print("\n\033[1;31;1mGame Over.\033[m AI2 \033[1;32;1mWins.\033[m")
        quit()
    if len(bot_4) == 0:
        print("\n\033[1;31;1mGame Over.\033[m AI3 \033[1;32;1mWins.\033[m")
        quit()







# Creating the deck
for i in range(len(colors)):
    for j in range(len(nums)):
        deck.append(UnoCard(colors[i],nums[j]))
    for j in range(1,len(nums)):
        deck.append(UnoCard(colors[i],nums[j]))
random.shuffle(deck)


# Dealing the cards
for b in range(7):
    player.append(deck[b])
    deck.remove(deck[b])

for b in range(7,14):
    bot_2.append(deck[b])
    deck.remove(deck[b])

for b in range(14,21):
    bot_3.append(deck[b])
    deck.remove(deck[b])

for b in range(21,28):
    bot_4.append(deck[b])
    deck.remove(deck[b])

def PlayCard():
    wanna_play = input("\nSelect the card number you wanna play or press 'd' for draw a card : ")
    if wanna_play == "D" or wanna_play == "d":
        player.append(deck[0])
        deck.remove(deck[0])
        if len(deck) < 36:
            DeckShuffle()
        print("\nCard at the middle is:", deck[-1])
        for i in range(len(player)):
            print(f"{i}) {player[i]}", end=" | ")
        PlayCard()
    else:
        if UnoCard.CanPlay(player[int(wanna_play)], deck[-1]):
            print(f"You played {player[int(wanna_play)]}")
            Cut(player,deck,player[int(wanna_play)])
        else:
            print("\nYou can't play that card.")
            for i in range(len(player)):
                print(f"{i}) {player[i]}", end=" | ")
            PlayCard()


def BotPlay(bot_i,b):
    a = 0

    while a <= len(bot_i) - 1 and b == 0:
        if UnoCard.CanPlay(bot_i[a],deck[-1]):
            if bot_i == bot_2:
                print(f"AI1 played {bot_i[a]}. AI1 has {len(bot_i)-1} cards.")
            if bot_i == bot_3:
                print(f"AI2 played {bot_i[a]}. AI2 has {len(bot_i)-1} cards.")
            if bot_i == bot_4:
                print(f"AI3 played {bot_i[a]}. AI3 has {len(bot_i)-1} cards.")
            Cut(bot_i, deck, bot_i[a])
            b = 72




        if a >= len(bot_i) - 1 and b != 72:
            bot_i.append(deck[0])
            deck.remove(deck[0])
            if bot_i == bot_2:
                print(f"AI1 drew a card. AI1 has {len(bot_i)} cards.")
            if bot_i == bot_3:
                print(f"AI2 drew a card. AI2 has {len(bot_i)} cards.")
            if bot_i == bot_4:
                print(f"AI3 drew a card. AI3 has {len(bot_i)} cards.")

            if UnoCard.CanPlay(bot_i[-1],deck[-1]):
                BotPlay(bot_i,0)
            else:
                continue
            b = 72
        a += 1


def DeckShuffle():
    the_one = deck[-1]
    for i in range(1, len(deck)):
        shuffled.append(deck[i])
        random.shuffle(shuffled)

    deck.clear()
    deck.extend(shuffled)
    deck.append(the_one)



# Starting to the game

start_menu = input("""
\033[1;30;1m⚀⚀⚀⚀⚀⚀⚀⚀\033[m\033[1;35;1mWelcome to the\033[m \033[1;32;1mU\033[m\033[1;31;1mN\033[m\033[1;34;1mO\033[m\033[1;30;1m⚀⚀⚀⚀⚀⚀⚀⚀\033[m
        Press \033[1;32;1m1\033[m to start the game.
             Press \033[1;31;1mq\033[m to quit.

Your Choice: """)

if start_menu == "1":
    print("\nCard at the middle is:", deck[-1], "\n")
    print("Your deck:")

    while True:
        for i in range(len(player)):
            print(f"{i}) {player[i]}", end=" | ")
        CheckDeck(deck,played_cards)
        PlayCard()
        CheckWinner()
        BotPlay(bot_2,0)
        CheckWinner()
        BotPlay(bot_3,0)
        CheckWinner()
        BotPlay(bot_4,0)
        CheckWinner()



if start_menu == "Q" or start_menu == "q":
    quit()
