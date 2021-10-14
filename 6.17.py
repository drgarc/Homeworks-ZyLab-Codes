#Daniel Garcia ; PSID 1601483

weak_password = input()
#store/build stronger password in the password variable
password = ''

for p in weak_password:
    if (p == 'i'):
        password += "!"
    elif (p == 'a'):
        password += "@"
    elif (p == 'm'):
        password += "M"
    elif (p == 'B'):
        password += "8"
    elif (p == 'o'):
        password += "."
    else:
        password += p

password += "q*s"
print(password)