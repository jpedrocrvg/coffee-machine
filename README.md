# Coffee Machine Simulator

This Python code simulates a basic coffee machine with a menu offering three popular drinks: espresso, latte, and cappuccino. Users can interact with the coffee machine, place orders, check resource status, and make transactions.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Functions](#functions)
- [Menu](#menu)
- [Resources](#resources)
- [Cash Register](#cash-register)
- [Coin Denominations](#coin-denominations)

## Features
1. **Menu:** Choose from a selection of drinks, each with its own set of ingredients and cost.
2. **Resource Management:** Keep track of available resources (water, milk, and coffee).
3. **Cash Register:** Track the total earnings from transactions.
4. **Coin Handling:** Accept user input for coins (penny, nickel, dime, quarter) to complete transactions.

## Usage
1. Run the code in a Python environment.
2. Follow the prompts to interact with the coffee machine.
3. Place orders by entering the name of the desired drink (espresso, latte, cappuccino).
4. Check the status of available resources using the 'report' command.
5. Insert coins when prompted, and the machine will dispense the ordered drink.

## Functions
- **buy_resources():** Replenish machine resources when triggered by the user.
- **report():** Display the current status of available resources and the cash register.
- **coffee_machine():** Main function simulating the coffee machine's operation.

## Menu
The menu includes the following drinks:
1. **Espresso**
    - Ingredients: Water (50ml), Coffee (18g)
    - Cost: $1.5

2. **Latte**
    - Ingredients: Water (200ml), Milk (150ml), Coffee (24g)
    - Cost: $2.5

3. **Cappuccino**
    - Ingredients: Water (250ml), Milk (100ml), Coffee (24g)
    - Cost: $3.0

## Resources
- **Water:** 300ml
- **Milk:** 200ml
- **Coffee:** 100g

## Cash Register
Track total earnings from transactions.

## Coin Denominations
- Penny: $0.01
- Nickel: $0.05
- Dime: $0.10
- Quarter: $0.25

Note: The code assumes a simplified input method for coin denominations and does not include extensive error handling for invalid inputs.
