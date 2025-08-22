from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

menu_list = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while machine_is_on:
    selection = input(f"What would you like? ({menu_list.get_items()}): ").lower()

    if selection == 'report':
        coffee.report()
        money.report()
    elif selection == 'off':
        machine_is_on = False
    else:
        drink = menu_list.find_drink(selection)
        coffee.is_resource_sufficient(drink)
        money.make_payment(drink.cost)
        coffee.make_coffee(drink)
