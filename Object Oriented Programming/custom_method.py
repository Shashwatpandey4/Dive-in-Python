class Customer:                                     #class created
    def __init__(self, name,gender,membership):                #constructor
        self.name = name
        self.gender = gender
        self.membership = membership
        print("done")

    def update_membership(self, new_membership):    #custom method
        self.membership = new_membership

    def __str__(self):
        return self.name + " " + self.gender


c = Customer("John","Male","gold")                         #object created
