#Daniel Garcia ; PSID 1601483

#Importing math for calculations
import math

#Prompt the user to input a wall's height and width. Calculate and output the wall's area (integer).
print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())

wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

#Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point). Assume a gallon of paint covers 350 square feet. Store this value in a variable. Output the amount of paint needed using the %f conversion specifier.
paint_needed = wall_area / 350
print('Paint needed: %.2f gallons' % paint_needed)
print('Cans needed:', math.ceil(paint_needed), 'can(s)')

#Extend by prompting the user for a color they want to paint the walls. Calculate and output the total cost of the paint cans depending on which color is chosen. Hint: Use a dictionary to associate each paint color with its respective cost. Red paint costs $35 per gallon can, blue paint costs $25 per gallon can, and green paint costs $23 per gallon can.
paint_colors = {'red': 35, 'blue': 75, 'green': 23}
color = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing', color, 'paint:' ' $' + str(paint_colors[color]))


