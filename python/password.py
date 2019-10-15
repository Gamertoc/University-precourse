password='Test123'
x = input('Password: ')
fails = 0;
while fails < 2:
    if len(x)!=len(password):
        x = input('Authentification failed. Please try again: ')
        fails = fails + 1
    else:
        for i in range(len(x)):
            if ord(x[i]) != ord(password[i]):
                x = input('Authentification failed. Please try again: ')
                fails = fails + 1
                break
        print('Access granted!')
        break
else:
    print('Authentification failure. Please contact a system admin to resolve.')
