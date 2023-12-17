import math


class Point:
    def __init__(self, coins, coins_after_bought, bags):
        self.coins = coins
        self.coins_after_bought = coins_after_bought
        self.bags = bags


def calc_all_possible_combinations():
    combinations = [[Point(0, 0, 0) for _ in range(days)] for _ in range(days)]

    for y in range(days):
        is_bag_bought = False
        for x in range(days):
            if x == 0:
                continue

            if y == 0:
                prev_x = combinations[y][x - 1]
                combinations[y][x] = Point(prev_x.coins + lord_profit, prev_x.coins, 0)
                continue

            prev_y = combinations[y - 1][x]
            if prev_y.coins_after_bought >= bag_price and not is_bag_bought:
                bags_bought = math.floor(prev_y.coins_after_bought / bag_price)
                coins_left = prev_y.coins_after_bought - bags_bought * bag_price
                total_bags = (bags_bought + prev_y.bags)
                combinations[y][x] = Point(coins_left + lord_profit + total_bags * bag_profit, coins_left, total_bags)
                is_bag_bought = True
                continue

            if not is_bag_bought:
                combinations[y][x] = prev_y
                continue

            prev_x = combinations[y][x - 1]
            combinations[y][x] = Point(prev_x.coins + lord_profit + prev_x.bags * bag_profit, prev_x.coins, prev_x.bags)

    return combinations


def calc_min_days():
    combinations = calc_all_possible_combinations()
    md = days + 1

    for y in range(days):
        for x in range(days):
            if combinations[y][x].coins >= target_coins:
                md = min(md, x)
                break

    return md


if __name__ == '__main__':
    with open('standard_input.txt', 'r') as file:
        inputData = file.read().split()

    target_coins = int(inputData[0])
    lord_profit = int(inputData[1])
    bag_price = int(inputData[2])
    bag_profit = int(inputData[3])

    days = math.ceil(target_coins / lord_profit) + 1
    min_days = calc_min_days()

    with open('standard_output.txt', 'w') as file:
        file.write(str(min_days))
