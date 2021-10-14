#Daniel Garcia ; PSID 1601483

#input from user and return date if input in correct format; else return empty string -- import datetime
import datetime
def extract_date(date):
    #if date = correct format correct_date will be change to 1 else 0
    global correct_date
    correct_date = 0
    #store new date in new_date
    new_date = ""

    #correct format must have comma
    if date.find(",") != -1:
        #year separated with comma
        mnth_day, year = date.split(',')

        #correct format must have space (" ") between month and day
        if mnth_day.find(" ") != -1:
            #separate month and day
            month, day = mnth_day.split(" ")

            correct_date = 1

            #removing whitespace
            day = day.strip()
            month = month.strip()
            year = year.strip()

            #new date format
            #appending month to new_date
            if month == "January":
                new_date = "1" + "/"
            elif month == "February":
                new_date = "2" + "/"
            elif month == "March":
                new_date = "3" + "/"
            elif month == "April":
                new_date = "4" + "/"
            elif month == "May":
                new_date = "5" + "/"
            elif month == "June":
                new_date = "6" + "/"
            elif month == "July":
                new_date = "7" + "/"
            elif month == "August":
                new_date = "8" + "/"
            elif month == "September":
                new_date = "9" + "/"
            elif month == "October":
                new_date = "10" + "/"
            elif month == "November":
                new_date = "11" + "/"
            elif month == "December":
                new_date = "12" + "/"
            else:
                correct_date = 0

            #adding day to new_date
            new_date += day + "/"

            #adding year to new_date
            new_date += year

    if correct_date == 1:
        return new_date
    else:
        return ""

#part A
#date = input()

#while (date != "-1"):
    #new_date = extract_date(date)

    #if new_date != "":
        #print(new_date)

    #print()
    #date = input()

#open input dates txtfile (B)
file = open('inputDates.txt', 'r')
file_dates = []

#reading input dates
file_dates = file.readlines()
file.close()

#removing whitespace
for i in range(len(file_dates) - 1):
    file_dates[i] = file_dates[i][:-1]

#part B
#for i in file_dates:
    #print(i)

#print("\nOutput\n")
#for i in file_dates:
    #if i == "-1":
        #break

    #new_date = extract_date(i)

    #if new_date != "":
        #print(new_date)

#open file for r parsed dates
file = open('parsedDates.txt', 'w')

for i in file_dates:
    if i == "-1":
        break
    else:
        new_date = extract_date(i)
        if new_date != "":
            file.write(new_date + "\n")
file.close()

#open file output from checking r parsed dates
file = open('parsedDates.txt', 'r')
file_parsed_dates = []

#reading parsed dates
file_parsed_dates = file.readlines()
file.close()

for i in file_dates:
    print(i)

print("\n")
for i in file_parsed_dates:
    print(i)