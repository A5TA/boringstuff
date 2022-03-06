'''
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''
import pyinputplus as pyip
price = 0
foodList = {'Bread': '', 'Protein': '', 'Cheese': '', 'topping': '', 'amount': 0}
print("Welcome to the Sandwich making program")

prices = {'wheat': 2, 'white': 1, 'sour dough': 3, 'chicken': 2, 'turkey': 3, 'ham': 2, 'tofu': 1,
          'cheddar': 1, 'swiss': 2, 'mozzarella': 3, 'mayo': 1, 'mustard': 1, 'lettuce': 1,
          'tomato': 1}


#Ask for Bread type
response = pyip.inputMenu( ['wheat', 'white', 'sourdough'], prompt = "What Type of Bread do you want: \n")
foodList['Bread'] = response

#Ask for Protein type
response = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = "What Type of Protein do you want: \n")
foodList['Protein'] = response

#Ask if they want Cheese
question = ""
question = pyip.inputYesNo(prompt = "Do you want cheese: \n")
if question == "yes":
    response = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella' ], prompt = "What Type of cheese: \n")
    foodList['Cheese'] = response
else:
    foodList['Cheese'] = 'None'

#Ask if they want the toppings mayo, mustard, lettuce, or tomato.
question = pyip.inputYesNo(prompt = "Do you want Toppings: \n")
if question == "yes":
    response = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato' ],prompt = "What Type of topping: \n")
    foodList['topping'] = response
else:
    foodList['topping'] = 'None'

#Ask for num of sandwiches
response = pyip.inputInt(prompt = "How many sandwiches do you want: \n", min= 1)
foodList['amount'] = response

#Calculate price

for food in foodList:
    for item in prices:
        if foodList[food] == "None":
            pass
        elif foodList[food] == item:
            price += prices[item]
price = price * foodList['amount']

print(foodList)
print(f"The price of your sandwich is ${price}.")