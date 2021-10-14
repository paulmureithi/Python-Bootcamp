from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu_items = Menu()

machine_is_on = True

while machine_is_on:
    order = menu_items.get_items()
    # prompt user to make an order
    user_choice = str(input(f'What would you like? ({menu_items.get_items()}): ')).lower()

    try:
        if user_choice == "off":
            machine_is_on = False
        elif user_choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:

            # find the drink
            drink = menu_items.find_drink(user_choice)
            if coffee_machine.is_resource_sufficient(drink):
                # process payments
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
    except AttributeError:
        print("Sorry wrong entry. Please try again!!")
        continue






