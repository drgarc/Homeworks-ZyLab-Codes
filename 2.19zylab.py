#Daniel Garcia ; PSID 1601483

#Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade. Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size.
print('Enter amount of lemon juice (in cups):')
lemon_juice = int(input())
print('Enter amount of water (in cups):')
water = int(input())
print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())
print('How many servings does this make?')
servings = float(input())
print()

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar')
print()

#Prompt the user to specify the desired number of servings. Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size.
print('How many servings would you like to make?')
print()
servings_quantity = int(input())

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_quantity), 'servings')
print('{:.2f}'.format(lemon_juice * servings_quantity / servings), 'cup(s) lemon juice')
print('{:.2f}'.format(water * servings_quantity / servings), 'cup(s) water')
print('{:.2f}'.format(agave_nectar * servings_quantity / servings), 'cup(s) agave nectar')
print()

#Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. Note: There are 16 cups in a gallon.
print('Lemonade ingredients - yields', '{:.2f}'.format(servings_quantity), 'servings')
print('{:.2f}'.format(lemon_juice * servings_quantity / servings / 16), 'gallon(s) lemon juice')
print('{:.2f}'.format(water * servings_quantity / servings / 16), 'gallon(s) water')
print('{:.2f}'.format(agave_nectar * servings_quantity / servings / 16), 'gallon(s) agave nectar')
