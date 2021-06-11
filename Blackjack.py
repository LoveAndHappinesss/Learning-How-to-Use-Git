from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + ' of ' + self.suit


class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):

        print_deck = ''

        for card in self.all_cards:

            print_deck += '/n' + card.__str__()

        return print_deck

    def shuffle_deck(self):

        shuffle(self.all_cards)

    def deal(self):

        single_card = self.all_cards.pop()

        return single_card


class Player():

    def __init__(self):

        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_card):

        if isinstance(new_card, list):

            self.hand.extend(new_card)

        else:

            self.hand.append(new_card)

        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value > 21 and self.aces > 0:

            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self):

        self.balance = 100
        self.bet = 0

    def win_bet(self):

        self.balance += self.bet

    def lose_bet(self):

        self.balance -= self.bet


def take_bet(chips):

    while True:

        try:

            chips.bet = int(input('Please place your bet: '))

        except ValueError:

            print('This is not a valid input')

        else:

            if chips.bet > chips.balance:

                print(f'You do not have sufficient funds for this bet. \
Your balance is {chips.balance} chips')

            else:

                break


def show_hands(player, dealer):

    print("\nDealer's hand: ")
    print(" - Card is hidden -")
    print('', dealer.hand[1])
    print("\nPlayer's hand: ",  *player.hand,  sep='\n')


def show_end_hands(player, dealer):

    print("\nDealer's hand: ",  *dealer.hand,  sep='\n')
    print("Value: ",  dealer.value)
    print("\nPlayer's hand: ",  *player.hand,  sep='\n')
    print("Value: ",  player.value)


def hit_or_stand(deck, player):

    global playing

    while playing:

        choice = input('\nWould you like to hit or stand (H or S): ').upper()

        if choice == 'H':

            hit(deck, player)

        elif choice == 'S':

            print("Player has chosen to stand. Dealer's turn")
            playing = False

        else:

            print('This is an invalid input')
            continue

        break


def hit(deck, player):

    player.add_card(deck.deal())
    player.adjust_for_aces()


def player_bust(player, dealer, chips):

    print("\nPlayer has gone bust!")
    chips.lose_bet()


def player_win(player, dealer, chips):

    print("\nPlayer has won!")
    chips.win_bet()


def dealer_bust(player, dealer, chips):

    print("\nDealer has gone bust!")
    chips.win_bet()


def dealer_win(player, dealer, chips):

    print("\nDealer has won!")
    chips.lose_bet()


def push(player, dealer):

    print('\nThe game is a push!')


print("Welcome to Blackjack! Your starting balance is 100 Chips. \
Dealer hits until 17.")

player_chips = Chips()

while True:

    playing = True

    deck = Deck()
    deck.shuffle_deck()

    player_hand = Player()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Player()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chips)
    show_hands(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck,  player_hand)
        show_hands(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value <= 17:

            hit(deck, dealer_hand)
            print("\nDealer hits")

        show_end_hands(player_hand, dealer_hand)

        if dealer_hand.value > 21:

            dealer_bust(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:

            player_win(player_hand, dealer_hand, player_chips)

        elif player_hand.value < dealer_hand.value:

            dealer_win(player_hand, dealer_hand, player_chips)

        else:

            push(player_hand, dealer_hand)

    print("Total chips: ", player_chips.balance)

    new_game = input("\nWould you like to play another \
hand? (Y or N): ").upper()

    if new_game == 'Y':

        playing = True
        continue

    else:

        print(f'Thank you for playing! Cashing out {player_chips.balance} chips \
for you.')

        break
