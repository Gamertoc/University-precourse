import math

def list(a, x):
    smallest = math.inf
    largest = 0
    five = []
    other = []
    for i in range(len(a)):
        if a[i] < smallest:
            smallest = a[i]
        elif a[i] > largest:
            largest = a[i]
    print('Smallest: ', smallest)
    print('Largest: ', largest)
    for i in range(len(a)):
        if a[i]%5 ==0:
            five.append(a[i])
        if a[i]%x ==0:
            other.append(a[i])
    print('Divide by 5: ', five)
    print('Divide by', x, ': ', other)
