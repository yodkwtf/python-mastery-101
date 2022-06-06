from random import shuffle

class Card:
    # class attributes
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # instance attributes
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
  # instance attributes
  def __init__(self):
    self.cards = []
    for suit in Card.suits:
      for value in Card.values:
        self.cards.append(Card(suit, value)) # returns "A of Clubs", "2 of Diamonds", etc. & runs 52 times

  def __repr__(self):
     return "Deck of {} cards".format(self.count())

  # instance methods
  def count(self):
    return len(self.cards)

  def shuffle(self):
    if self.count() < 52:
      raise ValueError("Only full decks can be shuffled")
    shuffle(self.cards)
    return self # convention to return self

  def _deal(self, n):
    if self.count() == 0:
      raise ValueError("All cards have been dealt")

    elif n > self.count():
      cards_to_remove = self.cards
      self.cards = []
      return cards_to_remove

    else:
      cards_to_remove = self.cards[-n:] # [1,2,3,4] & n=2 -> remove from 3 (-n) to end
      self.cards = self.cards[:-n] # [1,2,3,4] & n=2 -> keep starting to 3 (-n)
      return cards_to_remove

  def deal_card(self):
    return self._deal(1)[0] # cards_to_remove is a list

  def deal_hand(self, n):
    return self._deal(n)
