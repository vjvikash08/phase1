# class Cat:
#     def greet(self):
#         print("Cat says:Meow!")

# my_cat = Cat()
# my_cat.greet()

# __init__ method
class Cat:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        
    def greet(self):
        print(f"{self.name} says:Meow!")
        
my_cat = Cat("Zia",1,"grey")
my_cat.greet()
# Zia says:Meow!

# Access and change attributes:
print(my_cat.age) #1
my_cat.age = 2
print(my_cat.color) #grey