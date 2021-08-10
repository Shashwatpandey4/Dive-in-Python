class Customer:                                     #class created
    def __init__(self, name,gender):                #constructor
        self.name = name
        self.gender = gender
        print("done")


c = Customer("John","Male")                         #object created
print(c.name,c.gender)