from menu import MENU
from menu import resources

power_is_on = True
quarters_value = 0.25
dimes_value = 0.10
nickels_value = 0.05
pennies_value = 0.01
money = 0.0
success_transaction = False

# TODO 3. Print report.
def report():
    """To print report of current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# TODO 4. Check resources sufficient?
def check_resources(coffee):
    """To check resource"""
    for substance in MENU[coffee]['ingredients']:
        to_deduct = MENU[coffee]['ingredients'][substance]
        if to_deduct > resources[substance]:
            return False
        else:
            return True

# TODO 5. Process coins
def process_coins():
    global money

    coffee_cost = MENU[selection]['cost']

    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    quarters_total = quarters_value * quarters
    dimes_total = dimes_value * dimes
    nickels_total = nickels_value * nickels
    pennies_total = pennies_value * pennies

    inserted_coins = quarters_total + dimes_total + nickels_total + pennies_total

    # TODO 6. Check transaction successful?
    global success_transaction
    if inserted_coins > coffee_cost:
        change = inserted_coins - coffee_cost
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        money += coffee_cost
        success_transaction = True
    elif inserted_coins == coffee_cost:
        print("exact payment received")

        money += coffee_cost
        success_transaction = True
    else:
        print("Sorry that's not enough money. Money refunded.")
        money += 0

def make_coffee(coffee):
    for substance in MENU[coffee]['ingredients']:
        to_deduct = MENU[coffee]['ingredients'][substance]
        resources[substance] -= to_deduct
    print(f"Here is your {coffee} ☕. Enjoy!")


while power_is_on:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == "off":
        power_is_on = False
    elif selection == "report":
        report()
    else:
        sufficient = check_resources(selection)

        if sufficient:
            process_coins()
            if success_transaction:
                make_coffee(selection)
        else:
            print(f"Sorry, there is not enough water")
