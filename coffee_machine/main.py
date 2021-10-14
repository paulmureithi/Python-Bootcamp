from menu import MENU, resources

# create a money box for the machine
money = 0


def check_ingredients(drink_ingredients):
    """checks if there are enough resources to make that drink"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {drink_ingredients[item]}.")
            return False

    return True


def process_coins():
    """"Calculates and returns the monetary value of the coins inserted.
    quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"""
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    user_coins = 0
    user_coins += (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    return round(user_coins, 2)


def process_transaction(money_received, order_cost):
    """Checks if user has inserted enough money to purchase the drink they selected."""
    if money_received >= order_cost:
        change = round(money_received - order_cost, 2)
        global money
        money += order_cost
        print(f"Here is your {change}$ change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}")


machine_is_on = True
# TODO 1: Take user's input
while machine_is_on:
    user_input = str(input("What would you like? (1:Espresso 2:Latte 3:Cappuccino): ")).lower()

    if user_input == 'off':
        machine_is_on = False

    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        user_order = MENU[user_input]

        if check_ingredients(user_order["ingredients"]):
            payment = process_coins()
            if process_transaction(payment, user_order["cost"]):
                make_coffee(user_input, user_order["ingredients"])





