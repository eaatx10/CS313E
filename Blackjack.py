#  File: BlackJack.py
#  Description: This program simulates one round of blackjack.
#  Student's Name:Elias Ansari
#  Student's UT EID:eaa957
#  Course Name: CS 313E 
#  Unique Number: 50950
#######################################################################################################    
import random

class Deck ():
    
    def __init__ (self):

        # create suits and pip - loop to create deck with 52 cards
        self.deck = []
        self.printDeck = []
        suits = ["C", "S", "H", "D"]
        pips = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in range (4):
            for j in range(13):
                card = Card(suits[i], pips[j])
                self.deck.append(card)

    def __str__ (self):
        self.printDeck = []
        for i in range (len(self.deck)):
            self.printDeck.append(self.deck[i].card)
        return(self.printDeck)

    # method to shuffle deck
    def shuffle (self):
        random.shuffle(self.deck)
        
    # method to deal card from a deck
    def dealOne(self, Player):
        dealCard = self.deck[0]
        self.deck.pop(0)
        Player.hand.append(dealCard)
            

class Card ():

    suit = ["C", "S", "H", "D"]
    pip = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__ (self, suit, pip):
        self.suit = suit
        self.pip = pip
        self.card = self.pip + self.suit
    
    def __str__ (self):
        return (str(self.card))

class Player ():

    def __init__ (self):
        self.hand = []
        self.handTotal = 0

    def __str__ (self):
        x = ""
        for card in self.hand:
            x += str(card) + " "
        return x

    # give values to the pips
    def values(self):
        valuesDict = {"1":10, "2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
        sumValues = 0
        for i in range(len(self.hand)):
            j = self.hand[i].card[0]
            k = valuesDict[j]
            sumValues += k
        return sumValues

    # method to count aces   
    def score(self):
        values = {"1":10, "2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

        score = 0
        aces = 0
        for card in self.hand:
            if card.pip != "A":
                score += values[card.pip]
            else:
                aces += 1

        while aces != 0:
            if score + values["A"] <= 21:
                score += values["A"]
                aces -= 1
            else:
                score += 1
                aces -= 1
        self.handTotal = score
        return(self.handTotal)

# function that deals first cards to player and opponent    
def showHands(player, opponent):
    print("Dealer shows {} faceup".format(opponent.hand[1]))
    print("You show {} faceup".format(player.hand[1]))
    print("You go first.")

# function that deals with the player's moves
def playerMove(player, cardDeck):
    player.handTotal = player.values()
    lastRound = False
    stay = False
    while not lastRound:
        # player wins when having 21
        if player.handTotal == 21:
            print("21! My turn. . .")
            lastRound = True
            break
        else:
            # player keeps playing until choosing to stay
            while player.handTotal < 21:
                hand = []
                for k in range (len(player.hand)):
                    hand.append(player.hand[k].card)
                user = str(input("You hold {} for a total of {} \n1 (hit) or 2 (stay)? ".format(hand, player.handTotal)))
                while (user != "1") and (user != "2"):
                    user = input("1 (hit) or 2 (stay)? ")
                if user == "2":
                    stay = 1
                    lastRound = True
                    print("Now it's my turn. . . ")
                    break
                else:
                    cardDeck.dealOne(player)
                    player.handTotal = player.values()
                    print(player.handTotal)
            if player.handTotal > 21:
                print("Let me check for any aces.")
                oldScore = player.handTotal
                newScore = player.score()
                if oldScore != newScore:
                    if newScore > 21:
                        lastRound = True
                        print("Sorry, you busted. Your score is {}.".format(newScore))
                    else:
                        print("Hold on. I found some ace(s)!")
                else:
                    lastRound = True
                    print("Sorry, I couldn't find an(y) ace(s). You busted with a score of {}. Dealer wins.".format(newScore))
    return(player.score())
                    
# function that deals with dealer's moves                           
def dealerMove(opponent, totalNum, cardDeck):
    dealerHand = []
    for k in range (len(opponent.hand)):
        dealerHand.append(opponent.hand[k].card)
    opponentTotal = opponent.score()
    playerSum = totalNum
    win = False
    # player busts and dealer wins
    if playerSum > 21:
        win = True
        print("Player busts. Dealer wins with score of {} and a hand of {}.".format(opponentTotal, dealerHand))
    # dealer beats player score and wins
    if opponentTotal >= playerSum:
        win = True
        print("Dealer wins with a score of {} and a hand of {}.".format(opponentTotal, dealerHand))
    while not win:
        dealerHand = []
        cardDeck.dealOne(opponent)
        for k in range (len(opponent.hand)):
            dealerHand.append(opponent.hand[k].card)
        opponentTotal = opponent.score()
        # dealer has 21 and wins
        if opponentTotal == 21:
            win = True
            print("Dealer has 21. Dealer wins with a hand of {}.".format(dealerHand))
        # dealer busts and loses
        elif opponentTotal > 21:
            print("Dealer busted with score of {} and a hand of {}.".format(opponentTotal, dealerHand))
            break
        # dealer beats player score and wins
        elif opponentTotal > playerSum:
            win = True
            print("Dealer wins with a score of {} and a hand of {}.".format(opponentTotal, dealerHand))
        

def main ():

    # dictionary of values to each pip
    values = {"2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

    # print new deck
    cardDeck = Deck()
    print("New Deck:\n", cardDeck.__str__(), "\n")                 # for debugging purposes

    # print shuffled deck
    cardDeck.shuffle()
    print("Shuffled Deck:\n", cardDeck.__str__(), "\n")                 # for debugging purposes
    
    player = Player()
    opponent = Player()

    # deal cards to each player
    cardDeck.dealOne(opponent)
    cardDeck.dealOne(player)
    cardDeck.dealOne(opponent)
    cardDeck.dealOne(player)

    # print deck after dealing two cards
    print("Deck after dealing two cards each:\n", cardDeck.__str__(), "\n")
    
    showHands(opponent,player)      # remember not all cards are face up

    # call functions    
    totalNum = playerMove(player, cardDeck)
    dealerMove(opponent, totalNum, cardDeck)
    
main()
    
