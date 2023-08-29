MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
money = 0 
while choice != "off":
  
  if choice == "report":
    #print ( f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}")
    water = resources["water"]
    milk =  resources["milk"]
    coffee = resources["coffee"]
    print ( f"Water : {water}ml\nMilk : {milk}ml\nCoffee : {coffee}g")
    print ( f"Money : ${money}")
    choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
    if choice != "report":
      while resources ["water"] < MENU[choice]["ingredients"]["water"]:
        print ( "Sorry, there is not enough water.")
        choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
      while resources ["milk"] < MENU[choice]["ingredients"]["milk"]:
        print ( "Sorry, there is not enough milk.")
        choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
      while resources ["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print ( "Sorry, there is not enough coffee.")
        choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
      
  print ( "Please insert coins. ")
  quarters = int ( input ("how many quarters?: "))
  dimes = int ( input ("how many dimes?: "))
  nickles = int ( input ("how many nickles?: "))
  pennies = int ( input ("how many pennies?: "))
  
  
  def coins(choice, quarters, dimes, nickles, pennies):
    price =  ( MENU[choice]["cost"])
    #print ( price)
    quarters_1 = float( quarters * 0.25)
    dimes_1 = float ( dimes * 0.1 )
    nickles_1 = float ( nickles * 0.05)
    pennies_1 = float (pennies * 0.01)
    total =  quarters_1 + dimes_1 + nickles_1 + pennies_1
    back = total - price
    if total > price:
      print ( f"Here is ${round(back,2)} in change.")
      print ( f"Here is your {choice} ☕️. Enjoy!")
    else:
      print ( "Sorry that's not enough money. Money refunded. " )
      return "not"
  
  if coins(choice, quarters, dimes, nickles, pennies) != "not":
      money += ( MENU[choice]["cost"])
      resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
      resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
      resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
  
  
  choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
  if choice != "report":
    while resources ["water"] < MENU[choice]["ingredients"]["water"]:
      print ( "Sorry, there is not enough water.")
      choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
    while resources ["milk"] < MENU[choice]["ingredients"]["milk"]:
      print ( "Sorry, there is not enough milk.")
      choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
    while resources ["coffee"] < MENU[choice]["ingredients"]["coffee"]:
      print ( "Sorry, there is not enough coffee.")
      choice = input ( "What would you like? (espresso/latte/cappuccino):").lower()
