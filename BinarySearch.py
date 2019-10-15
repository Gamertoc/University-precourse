x = int(input('Number in range of 1 to 100: '))
n = 0
c = 0
mn=1
mx=100
while n != x:
    if c == 0:
        n=50
    elif n < x:
        print('Number is larger than', n)
        if mn < n:
            mn = n   
        n = int((n+mx)/2)
    elif n > x:
        print('Number is smaller than', n)
        if mx > n:
            mx = n
        n = int((n+mn)/2)
        
    c=c+1
else:
    print('Guessed after', c, 'tries! Number is', n)
