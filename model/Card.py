import abc


class Card(abc.ABC):
    def __init__(self, name: str, expansion: str, price: float):
        self._name = name
        self._expansion = expansion
        if isinstance(price, (float, int)):
            self._price = price

    def __eq__(self, other):
        for p_self, p_other in zip(vars(self).values(), vars(other).values()):
            if p_self != p_other:
                return False
        return True

    def __hash__(self):
        tmp = f'{self._name} {self._expansion} {self._price}'
        return int(''.join(str(ord(c)) for c in tmp))

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
        
    @property
    def expansion(self) -> str:
        return self._expansion
    
    @expansion.setter
    def expansion(self, expansion: str):
        self._expansion = expansion

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (float, int)):
            self._price = price

    @abc.abstractmethod
    def print(self):
        pass

    def see_on_scryfall(self) -> str:
        name = str.replace(self._name, " ", "%20")
        return f'https://scryfall.com/search?q=name%3A%22{name}%22+set%3A%22{self._expansion}%22&unique=cards&as=grid&order=name'
