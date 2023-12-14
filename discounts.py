from model import *


def get_discount_if_playset(order: Order) -> float:
    total_discount = 0
    for quantity in order.get_order().values():
        if quantity >= 4:
            total_discount += order.calculate_price() * 0.1
    return total_discount


def get_discount_if_value_above(order: Order) -> float:
    if order.calculate_price() > 100:
        return order.calculate_price() * 0.15
    return 0


