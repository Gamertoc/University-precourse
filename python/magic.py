x = int(input('One digit: '))
while (x/10)>=1:
    x = int(input('Try again! One digit: '))
else:
    x = (2*x + 10)/2 - x
print(int(x))
