#Daniel Garcia ; PSID 1601483

#Get a second user input into user_num1.
print('Enter integer:')
user_num1 = int(input())

#Output the user's input.
print('You entered:', user_num1)

#Output the input squared and cubed.
user_num_squared = user_num1 * user_num1
user_num_cubed = user_num1 ** 3
print(user_num1, 'squared is', user_num_squared)
print('And', user_num1, 'cubed is', user_num_cubed, '!!')

#Get a second user input into user_num2, and output the sum and product
print('Enter another integer:')
user_num2 = int(input())

print(user_num1, '+', user_num2, 'is', (user_num1 + user_num2))
print(user_num1, '*', user_num2, 'is', (user_num1 * user_num2))

