import math
def small(a):
    low = math.inf
    for i in range(len(a)):
        if a[i] < low:
            low = i
    return i

def read(x):
    file = open(x, "r")
    listn = []
    for l in file:
        z = file.readline().split
        print(z)
        for i in range(len(z)):
            listn.append(z[i])
    file.close()
    print(listn)
    sort = selsort(listn)
    print(sort)
    file = open(x, "w")
    for y in range(len(sort)):
        file.write(str(sort[y]))
    file.close()
        
    

def selsort(a):
    low = 0
    for i in range(len(a)):
        low = i
        j = i
        print(i, j)
        while j < len(a):
            if a[j] < a[low]:
                low = j
            j += 1
        print(i, low)
        t = a[i]
        a[i] = a[low]
        a[low] = t
    return a

        
