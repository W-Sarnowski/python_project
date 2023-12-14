from .Card import Card


class CreatureCard(Card):
    def print(self):
        print(f'{self._name} from {self._expansion} that costs {self._price} and is a {self._power}/{self._toughness}')

    def __init__(self, name: str, expansion: str, price: float, power: int, toughness: int):
        super().__init__(name, expansion, price)
        if isinstance(power, int):
            self._power = power
        if isinstance(toughness, int):
            self._toughness = toughness

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, power):
        if isinstance(power, int):
            self._power = power

    @property
    def toughness(self) -> int:
        return self._toughness

    @toughness.setter
    def toughness(self, toughness):
        if isinstance(toughness, int):
            self._toughness = toughness
