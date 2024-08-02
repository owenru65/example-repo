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


def print_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: ${resources["money"]}")


def check_resources(usr_resp, user_drink_dict):
    res_avail = True
    drink_requirements = user_drink_dict["ingredients"]

    required_water = drink_requirements["water"]
    required_coffee = drink_requirements["coffee"]

    if usr_resp == "espresso":
        required_milk = 0
    else:
        required_milk = drink_requirements["milk"]

    print(required_milk, required_coffee, required_water)

    if resources["water"] < required_water:
        print("Sorry, there is not enough water")
        res_avail = False
    elif resources["milk"] < required_milk:
        print("Sorry, there is not enough milk")
        res_avail = False
    if resources["coffee"] < required_coffee:
        print("Sorry, there is not enough coffee")
        res_avail = False

    return res_avail


def check_coins(cost):
    enough_money = True

    quarters = int(input("Input quarters: "))
    dimes = int(input("Input dimes: "))
    nickels = int(input("Input nickels: "))
    pennies = int(input("Input pennies: "))

    amt_input = float(((25 * quarters) + (10 * dimes) + (5 * nickels) + pennies) / 100)
    print(amt_input)
    if amt_input < cost:
        print("Sorry, that's not enough money. Money refunded.")
        enough_money = False
    elif amt_input > cost:
        print("Change refunded = ", amt_input - cost)

    return enough_money


def update_resources(usr_drink_dict, cost):
    drink_ingredients = usr_drink_dict["ingredients"]

    required_water = drink_ingredients["water"]
    required_coffee = drink_ingredients["coffee"]
    if user_response == "espresso":
        required_milk = 0
    else:
        required_milk = drink_ingredients["milk"]

    resources["water"] = resources["water"] - required_water
    resources["milk"] = resources["milk"] - required_milk
    resources["coffee"] = resources["coffee"] - required_coffee
    resources["money"] = resources["money"] + cost


# MAIN
serve_coffee = True
resource_available = True
drink_purchased = True
resources["money"] = 0.0

while serve_coffee:
    user_response = input("What would you like? (espresso/latte/cappuccino): ")
    if user_response == "off":
        print("Turning the coffee machine off.")
        break
    elif user_response == "report":
        print_report()
        continue
    elif user_response == "espresso" or user_response == "latte" or user_response == "cappuccino":
        user_drink_dict = MENU[user_response]
        drink_cost = user_drink_dict["cost"]
        print(f"Drink cost: {drink_cost}")
        resource_available = check_resources(user_response, user_drink_dict)
    else:
        print("Invalid response")
        continue

    if resource_available:
        drink_purchased = check_coins(drink_cost)
        if drink_purchased:
            print(f"Your {user_response} is on its way. Enjoy!!")
            update_resources(user_drink_dict, drink_cost)
    else:
        serve_coffee = False
