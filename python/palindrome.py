def palindrome_it(x):
    x=x.lower()
    for i in range(len(x)):
        if x[i] == x[-i-1]:
            continue
        else:
            return False
    return True

def palindrome_rec(x):
    x=x.lower()
    if not x:
        return True
    else:
        if x[0] == x[-1]:
            x = x[1:(-1)]
            return palindrome_rec(x)
        else:
            return False
    
