def faculty(x):
    if x > 1:
        return x*faculty(x-1)        
    else:
        return x
