class Cat:
    def __init__(self,name):
        self.name = name #private attribute
    
    @property
    def name(self):     #getter
        return self.name
    
    @name.setter
    def name(self,new_name):
        if len(new_name) >0:
            self.name = new_name
        else:
            print("Invalid name")
            
my_cat = Cat("Zia")
print(my_cat.name) #call getter - Zia 
my_cat.name = "Garfield"
print(my_cat.name) #Garfield
my_cat.name =""
