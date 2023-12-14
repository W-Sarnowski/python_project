from typing import Dict

from .Card import Card


class Order:
    def __init__(self, cards: Dict[Card, int]):
        for i, (card, count) in enumerate(cards.items()):
            if count < 1:
                raise Exception("Quantity can't be less than 1")
        self._cards = cards

    def calculate_price(self) -> float:
        price = 0
        for i, (card, count) in enumerate(self._cards.items()):
            price += card.price * count
        return price

    def add_card(self, card: Card, count: int = 1):
        if isinstance(count, int) and count > 0:
            if card in self._cards:
                self._cards[card] += count
            else:
                self._cards[card] = count

    def print(self):
        for i, card in enumerate(self._cards):
            card.print()
