file = open("input.txt", "r")
x = int(file.readline())
y = int(file.readline())
z = x*y
z = str(z)
print(x, y, z)
output = open("output.txt", "w")
output.write(z)
file.close()
output.close()
