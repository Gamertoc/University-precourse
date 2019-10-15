secretNumber=87
n=0
x=-1
while int(x)!= secretNumber:
    x=input('Guess: ')
    n=n+1
    if int(x)== secretNumber:
        break
    elif int(x)< secretNumber:    
        print('Too small! Try a larger one')
    else:
        print('Too large! Try a smaller one')
print('Congratulations! The number was', secretNumber, 'and you needed', n, 'tries!')
