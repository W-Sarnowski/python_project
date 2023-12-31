from typing import Dict

from .Card import Card


class Order:
    def __init__(self, cards: Dict[Card, int] = None):
        if cards is None:
            cards = {}
        for i, (card, count) in enumerate(cards.items()):
            if count < 1:
                raise Exception("Quantity can't be less than 1")
        self._cards = cards

    def get_order(self) -> Dict[Card, int]:
        return self._cards

    def calculate_price(self) -> float:
        price = 0
        for i, (card, count) in enumerate(self._cards.items()):
            price += card.price * count
        return price

    def add_cards(self, card: Card, count: int = 1):
        if isinstance(count, int) and count > 0:
            if card in self._cards:
                self._cards[card] += count
            else:
                self._cards[card] = count
        else:
            raise Exception("Can't add less than 1 card")

    def _has_cards(self, card: Card):
        for card_s in self._cards.keys():
            if card_s == card:
                return True
        return False

    def remove_card(self, card: Card, count: int = 1):
        if isinstance(count, int) and count > 0:
            if self._has_cards(card):
                if count < self._cards[card]:
                    self._cards[card] -= count
                elif count == self._cards[card]:
                    del self._cards[card]
                else:
                    raise Exception("Not enough cards to remove")
            else:
                raise Exception("Card is not in the order")
        else:
            raise Exception("Can't delete less than 1 card")

    def print(self):
        for i, card in enumerate(self._cards):
            card.print()
            print(f'{self._cards[card]} copies were ordered costing total of {"{:.2f}".format(card.price * self._cards[card])}')
