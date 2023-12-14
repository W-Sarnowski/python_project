from collections import deque
from typing import Callable

from .Order import Order


class OrderQueue:
    def __init__(self, orders: deque['Order'] = deque()):
        self._orders = orders

    @property
    def orders(self) -> deque['Order']:
        return self._orders

    def new_order(self, order: Order):
        self._orders.appendleft(order)

    def pop_order(self) -> Order | None:
        if len(self._orders) == 0:
            print("No orders to handle, returning None")
            return None
        return self._orders.pop()

    def get_orders_count(self) -> int:
        return len(self._orders)

    def print_order(self, index: int):
        print(f"Order {index}")
        self._orders[index].print()

    def print_queue(self):
        for i in range(len(self._orders)):
            self.print_order(i)

    def get_order_value(self, index: int) -> float:
        return self._orders[index].calculate_price()

    def get_total_value(self) -> float:
        total: float = 0
        for order in self._orders:
            total += order.calculate_price()
        return total

    def get_order_value_discounted(self, index: int, discount_fun: Callable[[Order], float]) -> float:
        order = self._orders[index]
        return order.calculate_price() - discount_fun(order)

    def get_queue_value_discounted(self, discount_fun: Callable[[Order], float]) -> float:
        total: float = 0
        for order in self._orders:
            total += order.calculate_price() - discount_fun(order)
        return total
