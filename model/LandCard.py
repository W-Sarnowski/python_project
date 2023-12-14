from .Card import Card


class LandCard(Card):
    def print(self):
        print(f'{self._name} from {self._expansion} that costs {self._price}')
        if self._is_basic:
            print('You can play any number of copies in your deck')

    def see_on_scryfall(self) -> str:
        if self._is_basic:
            return f'https://scryfall.com/search?q=name%3A%22{self._name}%22+set%3A%22{self._expansion}%22+unique%3Aprints&unique=cards&as=grid&order=name'
        super().see_on_scryfall()

    def __init__(self, name: str, expansion: str, price: float, is_basic: bool):
        super().__init__(name, expansion, price)
        if isinstance(is_basic, bool):
            self._is_basic = is_basic

    @property
    def is_basic(self) -> bool:
        return self._is_basic

    @is_basic.setter
    def is_basic(self, is_basic):
        if isinstance(is_basic, bool):
            self._is_basic = is_basic
