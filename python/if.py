x = float(input('A natural number: '))
y = int(x)
while x%y or x<0:
    x = float(input('Try again lol: '))
    y = int(x)
x = int(x)
if x == 1 or x == 2 or x == 3 or x == 5:
    print(2*x)
elif x == 4 or x == 6 or x == 7:
    print(4*x)
else:
    print(x)
