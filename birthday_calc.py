#Daniel Garcia ; PSID 1601483

#Prompt the user to enter the current date by month, day and year
print('Birthday Calculator\nPlease enter the current date')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

#Prompt the user to enter the birthday by month, day and year
print('Please enter you birthday')
user_month = int(input('Month: '))
user_day = int(input('Day: '))
user_year = int(input('Year: '))

#Output the age of the user in years
calc_year = current_year - user_year - 1

if (user_month < current_month):
    calc_year +=1
elif (current_month == user_month):
    if(user_day < current_day):
        calc_year +=1

#Output a "Happy Birthday!" message if the current date is the user's actual birthday.
if (current_month == user_month and current_day == user_day):
    print('Do you know what today is?? Happy Birthday friend!')
print('You are ' + str(calc_year) + ' years old.')
