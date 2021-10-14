#Daniel Garcia ; PSID 1601483

#requesting user input as str -- possible palindrome (poss_pal) & palindrome check (pal_check)
poss_pal = input()

#placing palindrome check (pal_check) into empty string
pal_check = ""

#string looping test
for i in range(len(poss_pal)):

    # Checking poss_pal[i] is not a space
    if(poss_pal[i] != ' '):

        #appending poss_pal[i] into pal_check
        pal_check = poss_pal[i] + pal_check

#testing that possible palindrome (poss_pal) and palindrome check (pal_check) are same or not
if (poss_pal == pal_check):
    print(poss_pal,"is a palindrome")
else:
    print(poss_pal,"is not a palindrome")