from typing import List

from .Card import Card
from .ColorEnum import Color


class TokenCard(Card):
    def print(self):
        tmp = f'{self._name} from {self._expansion} that costs {self._price} and is '
        if len(self._colors) == 0:
            tmp += 'colorless'
        for color in self._colors:
            tmp += color.value
        print(tmp)

    def see_on_scryfall(self) -> str:
        return f'https://scryfall.com/search?q=name%3A%22{self._name}%22+set%3A%22{self._expansion}%22+include%3Aextras+unique%3Aprints&unique=cards&as=grid&order=name'

    def __init__(self, name: str, expansion: str, price: float, colors: List[Color]):
        super().__init__(name, expansion, price)
        self._colors = list(dict.fromkeys(colors))

    @property
    def colors(self) -> List[Color]:
        return self._colors

    @colors.setter
    def colors(self, colors):
        self._colors = colors
