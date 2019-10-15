class Order:
    food = ""
    drink = ""

    def setFood(self,x):
        self.food = x

    def setDrink(self,x):
        self.drink = x

    def readOrder(self):
        print("You ordered", self.food, "with", self.drink)


    
