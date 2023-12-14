from collections import deque
from typing import Dict
from model import *


def handle_queue(queue: OrderQueue, storage: Storage):
    while queue.get_orders_count() > 0:
        handle_order(queue.pop_order(), storage)


def handle_order(order: Order, storage: Storage):
    print("Handling order")
    order.print()
    for i, (card, quantity) in enumerate(order.get_order().items()):
        storage.remove_card(card, quantity)
    print("Order handled\n")


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
