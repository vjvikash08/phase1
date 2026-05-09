class Cat:
    species ="Felis catus"
    
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        
cat1=Cat("Zia",1,"grey")
cat2 = Cat("Muchu",0,"grey")

print(cat1.species) #"Felis cetus"
print(cat2.species) #"Felis catus"
print(cat1.name) # Zia
print(cat2.name) #Muchu