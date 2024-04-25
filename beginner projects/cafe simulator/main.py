
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
pay_machine = MoneyMachine()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like? ({options}): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print("\n----------------")
        coffee_machine.report()
        pay_machine.report()
        print("----------------\n")

    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) == True:
            if pay_machine.make_payment(drink.cost) == True:
                coffee_machine.make_coffee(drink)


