from typing import List

from .ColorEnum import Color
from .CreatureCard import CreatureCard
from .SpellCard import SpellCard


class CreatureSpellCard(SpellCard, CreatureCard):

    def print(self):
        tmp = f'{self._name} from {self._expansion} that costs {self._price} and is a '
        if len(self._mana_pips) > 0:
            for mana_pip in self._mana_pips:
                if isinstance(mana_pip, int):
                    tmp.__add__(str(mana_pip))
                else:
                    tmp.__add__(mana_pip.value)
        tmp.__add__(f' {self._power}/{self._toughness}')

    def __init__(self, name: str, expansion: str, price: float, power: int, toughness: int, mana_pips: List[Color | int]):
        super().__init__(name, expansion, price, power, toughness)
        super().__init__(name, expansion, price, mana_pips)
