
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20  # Rupees
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30  # Rupees
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50  # Rupees
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: Rupees {money}")


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_money():
    try:
        return float(input("Please insert money in Rupees: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0


def transaction_successful(inserted_money, drink_cost):
    if inserted_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money > drink_cost:
        change = round(inserted_money - drink_cost, 2)
        print(f"Here is Rupees {change} in change.")
    return True



def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    global money
    money += MENU[drink_name]["cost"]
    print(f"Here is your {drink_name}. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Turning off the machine. Goodbye!")
        break
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_money()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please choose again.")
