class Cat:
    species = "Felics catus"        #class attributes - same for every cat
    
    def __init__(self,name,age,color):
        self.name = name         #instance attributes - different per cat
        self.age = age
        self.color = color
        
cat1 = Cat("Zia",1,"grey")
cat2 = Cat("Muchu",2,"grey")

print(cat1.species) #Felics catus
print(cat2.species) #Felics catus
print(Cat.species) #"Felics catus" - accessible from class too

print(cat1.name) #"Zia"
print(cat2.name) #"Muchu"