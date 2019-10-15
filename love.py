love = []
def fall_in_love(x, y):
    love.append((x, y))

def loves(x):
    for i in range(len(love)):
        v = love[i]
        if v[0] == x:
            print(v[1])

def pairs():
    told = []
    for i in range(len(love)):
        x = love[i]
        x = x[::-1]
        if x in love and not x in told and not love[i] in told:
            print(love[i])
            told.append(x)
