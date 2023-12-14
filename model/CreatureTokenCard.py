from typing import List

from .ColorEnum import Color
from .CreatureCard import CreatureCard
from .TokenCard import TokenCard


class CreatureTokenCard(CreatureCard):

    def print(self):
        tmp = f'{self._name} from {self._expansion} that costs {self._price} and is a {self._power}/{self._toughness} '
        if len(self._colors) == 0:
            tmp.__add__('colorless')
        for color in self._colors:
            tmp.__add__(color.value)
        print(tmp)

    def __init__(self, name: str, expansion: str, price: float, power: int, toughness: int, colors: List[Color]):
        self._colors = list(dict.fromkeys(colors))
        super().__init__(name, expansion, price, power, toughness)
