class Cat:
    def __init__(self,name):
        self.name = name 
    
    def __add__(self,other):
        return [self,other]                 #returns a list of both cats
    
cat1 = Cat("Zia")
cat2 = Cat("Weise")
family = cat1 + cat2
print([cat.name for cat in family]) #["Zia","Weise"]