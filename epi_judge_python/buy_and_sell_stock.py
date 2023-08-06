from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    min_price = 0
    profit = 0

    for price in range(prices):
        if price < min_price:
            min_price = price
            break

        current_profit = price - min_price
        if current_profit > profit:
            profit = current_profit

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
