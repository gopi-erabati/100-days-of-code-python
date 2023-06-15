from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): "
                        "").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        menuitem = menu.find_drink(user_choice)
        # check whether resources are sufficient
        if coffeemaker.is_resource_sufficient(
                menuitem) and moneymachine.make_payment(menuitem.cost):
            coffeemaker.make_coffee(menuitem)
