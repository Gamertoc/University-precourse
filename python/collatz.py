from statistics import mean
import numpy as np
def collatz(x, n):
    if x==1:
        return n
    elif x%2==0:
        return collatz(x/2, n+1)
    else:
        return collatz(3*x+1, n+1)

def listing(x):
    l = []
    for i in range(x):
        l.append(collatz(i+1, 0))
    mn = np.argmin(l)
    mx = np.argmax(l)
    avg = mean(l)
    print(mx, mn, avg)

def collatz_it(x):
    n=0
    while x != 1:
        if x%2==0:
            x = x/2
        else:
            x = 3*x+1
        n += 1
    print(n)

def fail():
    x = False
    n = 0
    while not x:
        n +=1
        t = n
        a = []
        if t % 100000000 == 0:
            print(t)
        if not t%2==0:
            while not t == 1 and not t<n:
                if t%2==0:
                    t = t/2
                    if not t in a:
                        a.append(t)
                    else:
                        x = True
                        break
                else:
                    t = 3*t+1
                    if not t in a:
                        a.append(t)
                    else:
                        x = True
                        break        
    print("Found it! Finally!")
    return n
        
        
