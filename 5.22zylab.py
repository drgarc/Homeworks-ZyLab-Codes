#Daniel Garcia ; PSID 1601483

#Attempted to write this code utilizing dictionaries which wold work great, but ran out of time so instead executing if-else statements

#Output a menu of automotive services and the corresponding cost of each service.
print('''Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12''')
print()

#Prompt the user for two services from the menu.
print('Select first service:')
service_1 = input()
print('Select second service:')
service_2 = input()
print()

#Output an invoice for the services selected. Output the cost for each service and the total cost
print("Davy's auto shop invoice")
print()

#Running assignment for total as user input changes
total = 0

#Parameters for Service 1 option
if service_1 == 'Oil change':
    print('Service 1: Oil change, $35')
    total = total + 35

elif service_1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total = total + 19

elif service_1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total = total + 7

elif service_1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total = total + 12

elif service_1 == '-':
    print('Service 1: No service')
    total = total + 0

else:
    print('Service 1: Invalid option')

#Parameters for Service 2 option
if service_2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total = total + 35

elif service_2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total = total + 19

elif service_2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total = total + 7

elif service_2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total = total + 12

elif service_2 == '-':
    print('Service 2: No service')
    total = total + 0

else:
    print('Service 2: Invalid option')

print()
print('Total: ${}'.format(total))