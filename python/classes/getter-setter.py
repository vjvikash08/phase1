class Cat:
    def __init__(self,name,age):
        self._name = name 
        self._age = age 
    
    def get_name(self):       #getter
        return self._name
    
    def set_name(self,new_name):   #setter
        if len(new_name) >0:
            self._name = new_name
        else:
            print("Invalid")
            
my_cat = Cat("zia",1)
my_cat.set_name("Garfield")
print(my_cat.get_name()) #"Garfield"
my_cat.set_name("")