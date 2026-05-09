class Cat:
    def __init__(self,name=None,age=None,color=None):
        self.name= name 
        self.age= age
        self.color = color
    
    def greet(self):
        print(f"{self.name} says:Meow!")
        
my_cat1 = Cat() #name=None, age=None, color=None
my_cat2 = Cat("Zia",1,"grey") #specific value
my_cat2.greet()
print(my_cat1.age) #None

# --------------------------------------
