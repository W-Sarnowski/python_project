from collections import deque
from typing import Dict, Callable

from model import *


def handle_queue(queue: OrderQueue, storage: Storage, discount: Callable[[Order], float] = None, currency_exchange: float = 1):
    queue_length = queue.get_orders_count()
    while queue_length > 0:
        order = queue.pop_order()
        handled = handle_order(order, storage, discount, currency_exchange)
        if not handled:
            queue.new_order(order)
        queue_length -= 1
    if queue.get_orders_count() > 0:
        print("There were some unhandled orders")
        queue.print_queue()


def handle_order(order: Order, storage: Storage, discount: Callable[[Order], float], multiplier: float):
    print("Checking if can be handled")
    if not storage.can_handle_order(order):
        print('Couldn\'t handle order\n')
        return False
    print("Handling order")
    order.print()
    for i, (card, quantity) in enumerate(order.get_order().items()):
        storage.remove_card(card, quantity)
    print("Order handled")
    value = order.calculate_price()
    if discount:
        value = OrderQueue.get_order_value_discounted(order, discount)
    change_currency = lambda val, multi : val * multi
    print(f"Total value was {change_currency(value, multiplier)}\n")
    return True


def gen_test_order_queue() -> OrderQueue:
    queue: OrderQueue = OrderQueue(deque([
        Order({
            CreatureSpellCard(
                'LLanowar Elves',
                'dom',
                0.19,
                1,
                1,
                [Color.Green]
            ): 4,
            LandCard(
                'Forest',
                'lci',
                1.2,
                True
            ): 26
        }),
        Order({
            CreatureTokenCard(
                'Spirit',
                'neo',
                0.05,
                1,
                1,
                []
            ): 6
        }),
        Order({
            LandCard(
                'Forest',
                'lci',
                1.2,
                True
            ): 1
        }),
        Order({
            SpellCard(
                'Enter the Infinite',
                'gtc',
                5,
                [8, Color.Blue, Color.Blue, Color.Blue, Color.Blue]
            ): 1
        })
    ]))
    return queue


def gen_test_storage() -> Storage:
    storage: Storage = Storage({
            CreatureSpellCard(
                'LLanowar Elves',
                'dom',
                0.19,
                1,
                1,
                [Color.Green]
            ): 10,
            CreatureTokenCard(
                'Spirit',
                'neo',
                0.05,
                1,
                1,
                []
            ): 20,
            LandCard(
                'Forest',
                'lci',
                1.2,
                True
            ): 100,
            SpellCard(
                'Enter the Infinite',
                'gtc',
                5,
                [8, Color.Blue, Color.Blue, Color.Blue, Color.Blue]
            ): 2
        })
    return storage
