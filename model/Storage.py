from typing import Dict
from model import Card


class Storage:
    def __init__(self, cards: Dict[Card, int]):
        self._cards = cards

    @property
    def cards(self) -> Dict[Card, int]:
        return self._cards

    @cards.setter
    def cards(self, cards: Dict[Card, int]):
        self._cards = cards

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
                    raise Exception("Not enough cards in storage")
            else:
                print(card)
                print(self._cards.keys())
                raise Exception(f"Card {card.name} from {card.expansion} is not in the storage")
        else:
            raise Exception("Can't delete less than 1 card")
