x = input('Text: ')
n = int(input('Offset: '))
s = ''
for i in range(len(x)):
    t = ord(x[i])
    if t >= 65:
        t = t-n
        if x[i].isupper():
            if t < 65:
                t = t + 26
            t = (t-65)%26+65
        else:
            if t < 97:
                t = t + 26
            t = (t-97)%26+97
        s = s + str(chr(t))
    else:
        s = s + x[i]
print(s)
    
