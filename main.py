from model import *
from functions import *
from discounts import *


def test():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    handle_queue(queue, storage)


def test_empty_queue():
    queue: OrderQueue = OrderQueue()
    storage: Storage = gen_test_storage()
    handle_queue(queue, storage)


def test_no_card_in_storage():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    storage.remove_card(LandCard(
                'Forest',
                'lci',
                1.2,
                True
            ), 100)
    handle_queue(queue, storage)


def test_discount():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    discount_fun = get_discount_if_playset
    handle_queue(queue, storage, discount_fun)


def test_discount_2():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    discount_fun = get_discount_if_value_above
    handle_queue(queue, storage, discount_fun)


def test_to_zloty():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    handle_queue(queue=queue, storage=storage, currency_exchange=4.3)


if __name__ == '__main__':
    test()
    test_empty_queue()
    test_no_card_in_storage()
    test_discount()
    test_discount_2()
    test_to_zloty()

