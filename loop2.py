x = input('Numbers please: ').split()
m=0
for i in range(len(x)):
    m = m + int(x[i])
m = m/len(x)
print(m)
