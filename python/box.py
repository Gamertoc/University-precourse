class Box:
    def __init__(self,x,y,z,c):
        self.length = x
        self.width = y
        self.height = z
        self.color = c
        print("You just created a box!")

    def volume(self):
        self.volume = self.length*self.width*self.height
        return self.volume

    def color(self):
        return self.color
