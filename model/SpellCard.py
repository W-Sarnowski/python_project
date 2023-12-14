from typing import List

from .Card import Card
from .ColorEnum import Color


class SpellCard(Card):
    def print(self):
        tmp = f'{self._name} from {self._expansion} that costs {self._price} and '
        if len(self._mana_pips) == 0:
            tmp.__add__('has no mana cost')
        else:
            tmp.__add__('has mana cost of ')
            for mana_pip in self._mana_pips:
                if isinstance(mana_pip, int):
                    tmp.__add__(str(mana_pip))
                else:
                    tmp.__add__(mana_pip.value)
        print(tmp)

    def __init__(self, name: str, expansion: str, price: float, mana_pips: List[Color | int]):
        super().__init__(name, expansion, price)
        number_count = len([i for i in mana_pips if isinstance(i, int)])
        if number_count <= 1:
            num = [i for i in range(len(mana_pips)) if isinstance(mana_pips[i], int)]
            if num:
                mana_pips.insert(0, mana_pips.pop(num[0]))
            if isinstance(mana_pips[0], int) and mana_pips[0] < 0:
                raise Exception("Only normal numbers allowed")
            self._mana_pips = mana_pips

    @property
    def mana_pips(self) -> List[Color | int]:
        return self._mana_pips

    @mana_pips.setter
    def mana_pips(self, mana_pips):
        number_count = len([i for i in mana_pips if isinstance(i, int)])
        if number_count <= 1:
            num = next(i for i, v in enumerate(mana_pips) if isinstance(v, int))
            mana_pips.insert(0, mana_pips.pop(mana_pips.index(num)))
            self._mana_pips = mana_pips
