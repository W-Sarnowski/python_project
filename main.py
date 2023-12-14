from model import *
from functions import *


def test():
    queue: OrderQueue = gen_test_order_queue()
    storage: Storage = gen_test_storage()
    handle_queue(queue, storage)


def test_empty_queue():
    queue: OrderQueue = OrderQueue()
    storage: Storage = gen_test_storage()
    handle_queue(queue, storage)


if __name__ == '__main__':
    test()
    test_empty_queue()

