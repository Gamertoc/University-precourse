def dividable_it(x, y):
    while x >= y:
        x -= y
    if x == 0:
        return True
    else:
        return False

def dividable_rec(x, y):
    if x >= y:
        x = dividable_rec(x-y, y)
    if x == 0:
        return True
    else:
        return False
