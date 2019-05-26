import random
suits=('Hearts','Spades','Clubs','Diamonds')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
       return f"{self.rank} of {self.suit}"

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffling(self):
       random.shuffle(self.deck)
class deal():

    def __init__(self):
        self.dealer=[]
        self.player=[]

        cards=0
        while cards <= 1:
            self.dealer.append(deck1.deck[0])
            deck1.deck.pop(0)
            self.player.append(deck1.deck[0])
            deck1.deck.pop(0)
            cards+=1

    def dealers_card(self):
        print("Here are the dealers card!")
        print('--------------------------')
        print('Hole_card ,',self.dealer[1])
        print('**************************')
        print('**************************')
    def players_card(self):
        print("These are your cards!")
        print('--------------------------')
        print(self.player[0],',',self.player[1])
        print('**************************')
bet_amount=0
class Chips():

    def __init__(self,total):
        self.total=total

    def bet(self):
        global bet_amount
        while True:
            bet_amount=int(input("Enter amount you want to bet "))
            if bet_amount<=self.total:
                break
            else:
                print("You do not have enough chips!")
        return bet_amount
    def win_hand(self,bet_amount):
        self.total+= bet_amount
        print('---------')
        print("You win!!")
        print(f"You got {self.total}")
    def loose_hand(self,bet_amount):
        self.total-=bet_amount
        print('---------')
        print('You lost.')
        print(f"You are left with {self.total}")

players_point=0
def hit_or_stand():
     global players_point
     players_total_points=[]
     print("Let me know if you want to hit or stand!")
     print("1.Hit\n2.Stand")
     while True:
       option=int(input("Enter 1 if you want to Hit and 2 if you want to Stand "))
       if option==1:
          cards_dealt.player.append(deck1.deck[0])
          deck1.deck.pop(0)
          print("Here are your cards!!")
          print('-------')
          for i in range(len(cards_dealt.player)):
              print(cards_dealt.player[i])
          print('**********************')
       elif option==2:
          points_players_list=list(map(str, cards_dealt.player))
          for i in points_players_list:
             players_total_points.append(values[i.split()[0]])
          break
     players_point=sum(players_total_points)
     print('----------')
     print(f"Total point of yours is {players_point}")
     print('----------')
dealers_point=0
def dealers_hit():
    global dealers_point
    points_list = []
    for i in cards_dealt.dealer:
        points_list.append(values[str(i).split()[0]])
    total_points=sum(points_list)
    while total_points <= 16:
         cards_dealt.dealer.append(deck1.deck[0])
         points_list.append(values[str(deck1.deck[0]).split()[0]])
         deck1.deck.pop(0)
         total_points=sum(points_list)
    print("Here are the dealers final set of cards!")
    print('--------')
    for i in map(str, cards_dealt.dealer):
        print(i)
    print('************************')
    dealers_point=total_points
    print(f"Dealer's total point is {dealers_point}")


print("Lets play!!")
Playing= True
while Playing:
    total=int(input("Please enter the total amount you want to play for "))
    bet1=Chips(total)
    bet1.bet()
    deck1=Deck()
    deck1.shuffling()
    cards_dealt=deal()
    cards_dealt.dealers_card()
    cards_dealt.players_card()
    hit_or_stand()
    if players_point > 21:
        print("You are Busted!")
        print("Dealer wins it all!")
        bet1.loose_hand(bet_amount)
        break
    elif players_point == 21:
        print("Blackjack!")
        bet1.win_hand(bet_amount)
        break
    elif players_point < 21:
            dealers_hit()
            if dealers_point > 21:
                print("Dealer is busted!")
                bet1.win_hand(bet_amount)
                break
            elif dealers_point==21:
                print("Dealer's Blackjack")
                bet1.loose_hand(bet_amount)
                break
            elif players_point < 21 and dealers_point < 21:
                 if  players_point > dealers_point:
                    bet1.win_hand(bet_amount)
                 elif dealers_point > players_point:
                    bet1.loose_hand(bet_amount)
                 else:
                    print("Nobody wins")
    Playing=False
