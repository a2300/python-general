import random

class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()

    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()        

    def to_tuple(self):
        return (self.suit, self.rank)    

class Deck:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)                             

    @staticmethod
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                cards.append(card)
        return cards


class Hand(Deck):
    """Represents a hand of cards."""

    def __init__(self, label=""):
        self.label = label
        self.cards = []

class BridgeHand(Hand):
    """Represents a bridge hand."""

    hcp_dict = {
        'Ace': 4,
        'King': 3,
        'Queen': 2,
        'Jack': 1,
    }

    def high_card_point_count(self):
        count = 0
        for card in self.cards:
            rank_name = Card.rank_names[card.rank]
            count += BridgeHand.hcp_dict.get(rank_name, 0)
        return count        

if __name__ == "__main__":
    # Example usage of the Card class
    card = Card(1, 12) 
    print(card) # Output: Queen of Diamonds

    queen = Card(1, 12)
    queen2 = Card(1, 12)
    print(queen2)

    print(card == queen2)  # Output: True - same suit and rank

    six = Card(1, 6)
    print(six)  # Output: 6 of Diamonds

    print(six < queen2)
    print(queen <= queen2)

    print("Card class defined with suit and rank names.")
    print("Suits:", card.suit_names)
    print("Ranks:", card.rank_names)


    cards = Deck.make_cards()
    deck = Deck(cards)
    print(len(deck.cards))

    small_deck = Deck([queen, six])
    print(small_deck)  # Output: Queen of Diamonds\n6 of Diamonds
    
    taken_card = small_deck.take_card()
    print("Taken card:", taken_card)
    print("Remaining cards in small deck:", small_deck)
    print(len(small_deck.cards))  # Output: 1 - one card left after taking one

    small_deck.put_card(Card(0, 3))  # Putting back a card
    print("After putting back the taken card:\n", small_deck)
    print(len(small_deck.cards))  # Output: 2 - two cards back

    deck.shuffle()  # Shuffle the deck
    print("Shuffled deck:")
    print(deck)  # Output: Random order of all cards in the deck

    deck.sort()  # Sort the deck
    print("Sorted deck:")
    for card in deck.cards[:4]:
        print(card)



    rank = 12
    rank_name = Card.rank_names[rank]
    score = BridgeHand.hcp_dict.get(rank_name, 0)
    print(f'Rank: {rank_name}, Score: {score}')  # Output: Rank: Queen, Score: 2 

    hand = BridgeHand('player 2')
    deck.shuffle()
    deck.move_cards(hand, 5)
    print(hand)
    print("High card point count:", hand.high_card_point_count())  # Output: High card point count: 0 - no cards yet


