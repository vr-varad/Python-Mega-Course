password = input('Enter Your Password: ')
has_lowercase = False
has_digit = False
has_uppercase = False
for i in password:
    if i.isupper():
        has_uppercase = True
    elif i.islower():
        has_lowercase = True
    elif i.isdigit():
        has_digit = True

if has_digit and has_lowercase and has_uppercase and len(password)>8:
    print('Strong Password')
else:
    print('Weak Password')