import numpy as np

x = int(input('Range please: '))
i=0
a = np.zeros((x, x))
while i < x:
    j=0
    while j < x:
        a[i, j]=(i+1)*(j+1)
        j=j+1
    i=i+1
print(a)
