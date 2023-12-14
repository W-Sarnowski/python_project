from typing import List

from .ColorEnum import Color
from .CreatureCard import CreatureCard
from .SpellCard import SpellCard


class CreatureSpellCard(CreatureCard):

    def print(self):
        tmp = f'{self._name} from {self._expansion} that costs {self._price} and is a '
        if len(self._mana_pips) > 0:
            for mana_pip in self._mana_pips:
                if isinstance(mana_pip, int):
                    tmp += str(mana_pip)
                else:
                    tmp += mana_pip.value
        tmp += f' {self._power}/{self._toughness}'
        print(tmp)

    def __init__(self, name: str, expansion: str, price: float, power: int, toughness: int, mana_pips: List[Color | int]):
        super().__init__(name, expansion, price, power, toughness)
        number_count = len([i for i in mana_pips if isinstance(i, int)])
        if number_count <= 1:
            num = [i for i in range(len(mana_pips)) if isinstance(mana_pips[i], int)]
            if num:
                mana_pips.insert(0, mana_pips.pop(num[0]))
            if isinstance(mana_pips[0], int) and mana_pips[0] < 0:
                raise Exception("Only normal numbers allowed")
            self._mana_pips = mana_pips
