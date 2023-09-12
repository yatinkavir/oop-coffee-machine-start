from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_machine = CoffeeMaker()
money_mc = MoneyMachine()

while is_on:
    # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino/):
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off" :
        is_on = False
    # TODO 3: Print report.
    elif choice == "report":
        coffee_machine.report()
        money_mc.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 4: Check resources sufficient.
        if drink and coffee_machine.is_resource_sufficient(drink):
            # TODO 5 and 6: Process coins and check transaction successful.
            success = money_mc.make_payment(drink.cost)
            if success:
                # TODO 7: Make coffee and update resources.
                coffee_machine.make_coffee(drink)
