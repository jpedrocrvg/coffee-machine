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

cash_register = 0

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

def buy_resources():
  global resources, cash_register
  cash_register -= 2
  resources['water']+=300
  resources['milk']+=200
  resources['coffee']+=100

def report():
  for item, quantity in resources.items():
      print(f'{item}: {quantity}ml')
  print(f'Cash Register: ${cash_register}')
  
def coffee_machine():
  global penny, nickel, dime, quarter, error, cash_register, resources, MENU


  while True:
      order = input('What would you like? (espresso/latte/cappuccino) ')
      if order == 'report':
          report()
      elif order in ['espresso', 'latte', 'cappuccino']:
          if order == 'espresso':
              required_amount = 1.50
              if resources['water'] < MENU['espresso']['ingredients']['water'] or \
                 resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                  print('Not enough resources. Buying resources...')
                  buy_resources()
                  continue
              resources['water'] -= MENU['espresso']['ingredients']['water']
              resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
          elif order == 'latte':
              required_amount = 2.50
              if resources['water'] < MENU['latte']['ingredients']['water'] or \
                 resources['milk'] < MENU['latte']['ingredients']['milk'] or \
                 resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                  print('Not enough resources. Buying resources...')
                  buy_resources()
                  continue
              resources['water'] -= MENU['latte']['ingredients']['water']
              resources['milk'] -= MENU['latte']['ingredients']['milk']
              resources['coffee'] -= MENU['latte']['ingredients']['coffee']
          elif order == 'cappuccino':
              required_amount = 3.00
              if resources['water'] < MENU['cappuccino']['ingredients']['water'] or \
                 resources['milk'] < MENU['cappuccino']['ingredients']['milk'] or \
                 resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                  print('Not enough resources. Buying resources...')
                  buy_resources()
                  continue
              resources['water'] -= MENU['cappuccino']['ingredients']['water']
              resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
              resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
          inserted_amount = 0
          while inserted_amount < required_amount:
              print('Please, insert coins.')
              penny_order = int(input('How many pennies? '))
              penny1 = penny_order * penny
              nickel_order = int(input('How many nickels? '))
              nickel1 = nickel_order * nickel
              dime_order = int(input('How many dimes? '))
              dime1 = dime_order * dime
              quarter_order = int(input('how many quarters? '))
              quarter1 = quarter_order * quarter
              sum_coins = dime1 + quarter1 + nickel1 + penny1
              rounded_sum = round(sum_coins, 3)
              print(f'Total: ${rounded_sum}')
  
              inserted_amount += rounded_sum
              if inserted_amount < required_amount:
                  print('You have to insert more coins.')
  
          if inserted_amount > required_amount:
              change = inserted_amount - required_amount
              print(f"Your change is ${round(change, 3)}\nHere's your order. Enjoy it! ☕")
              cash_register += inserted_amount - change
          elif inserted_amount == required_amount:
              print("Here's your order. Enjoy it! ☕")
              cash_register += inserted_amount
      else:
          print('Invalid word. Try again.')
          continue




coffee_machine()
