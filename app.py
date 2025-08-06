water = 300
milk = 200
coffee = 100
money = 0

MENU = {
    "green tea": {
        "ingredients": {"water": 100},  
        "cost": 20
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 60
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 80
    }
}

while True:
    choice = input("What would you like? (green tea/latte/cappuccino): ").lower()
    
    if choice == "off":
        print("Turning off the machine.")
        break

    elif choice == "report":
        print(f"\n--- Machine Report ---")
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ₹{money}\n")

    elif choice in MENU:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        can_make = True
        if ingredients.get("water", 0) > water:
            print(" Sorry, not enough water.")
            can_make = False
        if ingredients.get("milk", 0) > milk:
            print(" Sorry, not enough milk.")
            can_make = False
        if ingredients.get("coffee", 0) > coffee:
            print("Sorry, not enough coffee.")
            can_make = False

        if can_make:
            print("Please insert coins (₹1, ₹2, ₹5, ₹10).")
            try:
                one_rs = int(input("How many ₹1 coins?: ")) * 1
                two_rs = int(input("How many ₹2 coins?: ")) * 2
                five_rs = int(input("How many ₹5 coins?: ")) * 5
                ten_rs = int(input("How many ₹10 coins?: ")) * 10
            except ValueError:
                print(" Invalid input. Coins must be numbers.")
                continue

            total_inserted = one_rs + two_rs + five_rs + ten_rs

            if total_inserted < cost:
                print(f" Not enough money. ₹{total_inserted} refunded.\n")
            else:
                change = total_inserted - cost
                if change > 0:
                    print(f" Here is ₹{change} in change.")
                
                money += cost
                water -= ingredients.get("water", 0)
                milk -= ingredients.get("milk", 0)
                coffee -= ingredients.get("coffee", 0)

                print(f" Here is your {choice}. Enjoy")
