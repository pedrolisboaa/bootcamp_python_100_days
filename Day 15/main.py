from operacoes import *

global MONEY
MONEY = 0

options = ['espresso', 'latte', 'cappuccino', 'report']
info_report = f'Water: {INGREDIENTS["water"]}ml \nMilk: {INGREDIENTS["milk"]}ml \nCoffee: {INGREDIENTS["coffee"]}g ' \
              f'\nMoney: ${MONEY:.2f} '


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= INGREDIENTS[item]:
            print(f'Sorry the is not enough {item}')
            return False
    return True


def process_coins():
    print('Please insert coins.')
    total = int(input('how many quarters: ')) * 0.25
    total += int(input('how many dimes: ')) * 0.1
    total += int(input('how many nickles: ')) * 0.05
    total += int(input('how many pennies: ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global MONEY
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in changes.')
        MONEY += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        INGREDIENTS[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕')



while True:

    asking = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if asking == 'off':
        print(f'Machine off...')
        break

    if asking == 'report':
        print(info_report)

    if asking in options:
        drink = MENU[asking]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(asking, drink['ingredients'])

