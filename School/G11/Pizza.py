running = True

# Global Options
SIZES = {'small': [7.58, 0], 'medium': [9.69, 1], 'large': [12.09, 2], 'jumbo': [17.99, 3], 'party': [20.29, 4]} # [Price, ID]
TOPPINGS = {'pepperoni': [0, False], 'bacon': [0, True], 'sausage': [0, False], 'mushroom': [1, False], 'black olive': [1, False], 'green pepper': [1, False]} # [Group, Special]

TOPPING_PRICES = [[1.6, 2.05, 2.35, 3.15, 3.30], [1.95, 2.25, 2.65, 3.49, 3.69]] # 0: No Special - 1: Special [Inc size]

def ask(question, options, show = True):
    answer = False
    o = "" # Choices to show, only if show = true
    if show:
        o = " (" + ', '.join([str(lst).title() for lst in options]) + ")"
    while True:
        a = input(question + o + ": ").lower() # User input
        if a.isdigit(): # Allow users to pick via number too
            a = int(a) - 1 # Set to an int
            if a in range(0, len(options)):
                a = options[a] # Set to value so next function completes
        if a in options: # Is option valid?
            answer = a
            break
        print("Not a valid option, try again!") # Nope
    return answer # Return answer

def splitter():
    print("---------------------------------------------------")
    
# Only do while running, used for confirmation.
while running:
    PIZZA = {} # Pizza config
    DELIVERY = {} # Delivery config
    TOTAL = 0

    # Start title
    print("                    MAKAN PIZZA                    ")
    splitter()

    # Delivery or pickup?
    DELIVERY['type'] = ask("Type of order", ['delivery', 'pickup'])

    while True:
        DELIVERY['location'] = input("Location of " + DELIVERY['type'] + ": ") # Need a location
        # Did they leave it blank?
        if DELIVERY['location']:
            break
        else:
            print("Please enter a valid location!")

    # If delivery, ask for special instructions
    if DELIVERY['type'] == "delivery":
        DELIVERY['special_instructions'] = input("Special instructions (Blank for None): ")
        # Do they have special instructions?
        if not DELIVERY['special_instructions']:
            DELIVERY['special_instructions'] = "None"
    
    splitter()

    # Size of the pizza
    PIZZA['size'] = ask("Select the size", ['small', 'medium', 'large', 'jumbo', 'party'])

    # Dough type
    PIZZA['dough'] = ask("Select dough type", ['regular', 'whole wheat', 'carbone'])

    # Type of sauce
    PIZZA['sauce'] = ask("Type of sauce", ['tomato', 'pesto', 'bbq sauce', 'no sauce'])

    # Type of primary cheese
    PIZZA['cheese'] = ask("Type of cheese", ['mozzarella', 'cheddar', 'dairy-free', 'no cheese'])

    splitter()

    # Pick your topping section!
    print("Pick your Toppings!", end = "")
    count = -1 # Category count
    for i in TOPPINGS:
        start = "" # Used for the comma

        # Check category and print to new line if so.
        if TOPPINGS[i][0] != count:
            count = TOPPINGS[i][0]
            print("\n--> ", end = "")
        else:
            start = ", " # Split toppings
        print(start + i.title(), end = "") # Print topping 

        # Special topping?
        if TOPPINGS[i][1]:
            print(" (*)", end = "")
    print() # New line

    # Extra functions
    print("--> Typing in list will show current toppings.")
    print("--> Retyping in a topping will remove it.")
    print("--> Press enter once you're done!")

    # Topping selector
    PIZZA['toppings'] = []
    while True:
        top = input("Pick your topping: ") # Get input
        if top == "list": # Want a list of toppings.
            if not len(PIZZA['toppings']): # Do they have toppings?
                print("You have no toppings!")
            else:
                for i in PIZZA['toppings']: # Go through and print toppings.
                    print("--> ", i.title())
        elif not top: # Done picking.
            break
        else: # Picked a topping?
            if top.endswith('s'): # If it ends with s, remove and check (sausages -> sausage)
                top = top[:-1]
            if top in TOPPINGS:
                if top in PIZZA['toppings']:
                    print("Topping", top.title(), "has been removed from your order.")
                    PIZZA['toppings'].remove(top) # Remove topping
                else:
                    print("Topping", top.title(), "has been added to your order.")
                    PIZZA['toppings'].append(top) # Add topping
            else:
                print("That topping does not exist!")
    
    splitter()
    print("          MAKAN PIZZA ORDER CONFIRMATION           ")
    splitter()

    # Calculate the price of order and print.
    print(PIZZA['size'].title() + " Pizza (CAD$" + str(SIZES[PIZZA['size']][0]) + ")")
    TOTAL += SIZES[PIZZA['size']][0] # Price of size

    # Free Things
    print("--> " + PIZZA['dough'].title() + " (FREE)")
    print("--> " + PIZZA['sauce'].title() + " (FREE)")
    print("--> " + PIZZA['cheese'].title() + " (FREE)")

    # Toppings
    if PIZZA['toppings']:
        print("--> Toppings:") # If they have any toppings, print title
        # Go through all the toppings
        for i in PIZZA['toppings']:
            if TOPPINGS[i][1]:
                tpp = TOPPING_PRICES[1][SIZES[PIZZA['size']][1]] # Special pricing
            else:
                tpp = TOPPING_PRICES[0][SIZES[PIZZA['size']][1]] # Non-Special pricing
            print("   --> " + i.title() + " (CAD$" + format(tpp, '.2f') + ")") # Print the topping name and price
            TOTAL += tpp # Add price of topping to total
    
    splitter()
    print("Sub-Total:       CAD$" + format(TOTAL, '.2f')) # total
    
    # Delivery has delivery fee (Fixed $3.50)
    if DELIVERY['type'] == "delivery": 
        print("Delivery Fee:    CAD$3.50")
        TOTAL += 3.5

    # Calculate and add tax
    TAX = round(TOTAL * 0.13, 2)
    TOTAL += TAX
    print("Tax:             CAD$" + format(TAX, '.2f'))
    print("Total:           CAD$" + format(TOTAL, '.2f'))

    splitter()
    CONFIRM = ask("Do you wish to confirm this order", ['yes', 'no'])
    splitter()

    # Done?
    if CONFIRM == "yes":
        break

# Final order print
print("Your order is on the way, we'll be there in 45 minutes or you get a refund!")
if DELIVERY['type'] == "delivery": # Did they get delivery?
    print("Delivery to:", DELIVERY['location'], "(Special Instructions:", DELIVERY['special_instructions'] + ")")
else:
    print("Pickup at:", DELIVERY['location'])
splitter()