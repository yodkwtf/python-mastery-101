import unittest
from app import Card, Deck

class CardTests(unittest.TestCase):
  # set everything up
  def setUp(self):
    self.card = Card("Clubs", "A")

  def test_init(self):
    """card should have suit and value"""
    self.assertEqual(self.card.suit, "Clubs")
    self.assertEqual(self.card.value, "A")

  def test_repr(self):
    """repr should return string in specified way"""
    self.assertEqual(repr(self.card), "A of Clubs")



class DeckTests(unittest.TestCase):
  # set up
  def setUp(self):
    self.deck = Deck()

  def test_init(self):
    """deck should have 52 cards"""
    self.assertEqual(len(self.deck.cards), 52)

  def test_repr(self):
    """repr should return string in specified way"""
    self.assertEqual(repr(self.deck), "Deck of 52 cards")

  def test_count(self):
    """should return a count of cards"""
    self.assertEqual(len(self.deck.cards), 52)
    self.deck.cards.pop()
    self.assertEqual(len(self.deck.cards), 51)


# calling unittest
if __name__ == '__main__':
  unittest.main()