#Daniel Garcia ; PSID 1601483

#exact_change function definition
def exact_change(user_total):
    if (user_total <= 0):
        #dollars,quarters,dimes,nickels,pennies
        return None, None, None, None, None
    else:
        #dollar conversion;remainder
        num_dollars = user_total // 100
        user_total %= 100

        #quarter conversion;remainder
        num_quarters = user_total // 25
        user_total %= 25

        #dime conversion;remainder
        num_dimes = user_total // 10
        user_total %= 10

        #nickel conversion;remainder
        num_nickels = user_total // 5

        num_pennies = user_total % 5

        return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

#mainpy file name required function
if __name__ == '__main__':
    #user int input
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if(num_dollars == None):
        print("no change")
    else:
        if num_dollars > 0:
            if num_dollars == 1:
                print('%d dollar' % num_dollars)
            else:
                print('%d dollars' % num_dollars)

        if num_quarters > 0:
            if num_quarters == 1:
                print('%d quarter' % num_quarters)
            else:
                print('%d quarters' % num_quarters)

        if num_dimes > 0:
            if num_dimes == 1:
                print('%d dime' % num_dimes)
            else:
                print('%d dimes' % num_dimes)

        if num_nickels > 0:
            if num_nickels == 1:
                print('%d nickel' % num_nickels)
            else:
                print('%d nickels' % num_nickels)

        if num_pennies > 0:
            if num_pennies == 1:
                print('%d penny' % num_pennies)
            else:
                print('%d pennies' % num_pennies)