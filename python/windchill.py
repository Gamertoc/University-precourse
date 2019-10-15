import math
T = float(input('Temperature in °C (integer): '))
v = float(input('Speed in km/h (integer): '))
while T != int(T):
    T = input('Try again! Temperature in °C: ')    
while v != int(v):
    v = input('Try again! Speed in km/h: ')
Wold = 33 + (.478 + .237*math.sqrt(v) - .0124*v) * (T-33)
Wnew = 13.12 + .6215*T -11.37*(v**0.16) + .3965*T*(v**0.16)

Wold = (int(Wold*10))/10
Wnew = (int(Wnew*10))/10
print('Windchill temperature in °C (old method): ', Wold)
print('Windchill temperature in °C (new method): ', Wnew)
