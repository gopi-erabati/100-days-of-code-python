MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# function to check the available resources depending upon the choice of user
def is_resources_available(choice):
    for ingred_menu, ingred_val in MENU[choice]['ingredients'].items():
        if resources[ingred_menu] < ingred_val:
            return False, ingred_menu
        else:
            return True, None


# function to check if transaction is successful
def is_transaction_successful(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + \
                     pennies * 0.01

    # check if money inserted is greater than cost of coffee
    if money_inserted > MENU[choice]['cost']:
        change = round(money_inserted - MENU[choice]['cost'], 2)
        print(f"Here is ${change} in change")
        return True
    elif money_inserted == MENU[choice]['cost']:
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False


def update_resources_money(choice):
    """ Function to update resources and money if transaction is successful"""
    resources['money'] += MENU[choice]['cost']
    for ingred_menu, ingred_val in MENU[choice]['ingredients'].items():
        resources[ingred_menu] -= ingred_val


def deliver_coffee(choice):
    """ Function to check if resources are available, check transaction and
    update resources and money"""
    # check the ingredients for preparing espresso
    resources_status, res_not_available = is_resources_available(user_choice)
    # if there are no resources then
    if not resources_status:
        print(f"Sorry, there is no enough {res_not_available}")
    else:
        transaction_status = is_transaction_successful(user_choice)
        if transaction_status:
            # update the resources and money
            update_resources_money(user_choice)
            print(f"Here is you {user_choice}. Enjoy!")


def print_report():
    """ Function to print the report of all resources"""
    for key, val in resources.items():
        if key in ['water', 'milk']:
            print(f"{key.title()}: {val} ml")
        elif key == 'coffee':
            print(f"{key.title()}: {val} g")
        else:
            print(f"{key.title()}: ${val}")


resources['money'] = 0
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): "
                        "").lower()
    if user_choice in ['espresso', 'latte', 'cappuccino']:
        deliver_coffee(user_choice)
    elif user_choice == 'report':
        print_report()
    elif user_choice == 'off':
        is_on = False
