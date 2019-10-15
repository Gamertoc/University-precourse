x = int(input('Range: '))
i=1
test = True
while i <= x:
    j=1
    while j < i:
        if i%j==0 and j!=1 and j!=i:
            test = False
            break
        j=j+1
    if test:
        print(i)
    test = True
    i=i+1
