from pydoc import describe


def greet():
    print("Hello humans")
    
# parameters and arguments 
def greet_by_name(name):
    print("Hello",name)
    
greet_by_name("Zia")
greet_by_name("Weisey")

# multiple parameters 
def feed_pet(pet_name,food):
    print("Feeding",pet_name,"some delicious",food)
    
feed_pet("Zia","tuna")
feed_pet("Weisey","chicken")

# Return Value
def return_nothing():
    print("hi")
    
val = return_nothing()
print(val)

def get_pet_info():
    pet_name =input("Pet's name")
    if pet_name.lower() == "quit":
        return None
    species = input("Species?")
    food = input("Food?")
    return (pet_name,species,food)

# VARIABLE SCOPING
def feed_cat():
    food = "tuna" #local variable
    print("Feeding cat with food",food)
    
feed_cat()
# print(food)

# global scope - variables defined outside of any function
food = "tuna" # global variable
def feed_cat():
    global food # use the global variable
    food = "salmon" # local variable
    print("Feeding cat with food",food)
    
feed_cat()
print(food) #salmon
# ---------------default parameter-----------
def greet_friend(name,greeting="Hello"):
    print(greeting,name)
greet_friend("Zia");
greet_friend("weise","Hi")

# keyword arguments ----------------------
def describe_pet(pet_name,species,age):
    print(f"{pet_name} is a {species} and is {age} years old")
    
describe_pet(species="deser",pet_name="weise",age=7)
# ---------------------
# args -----variable number of positional arguments 
# --------------------
def show_off(*args,**kwargs):
    print("Positional args:",args)
    print("Keyword args:",kwargs)
    
show_off("Zia","Weise",toy="feather wand", snack="tuna")
# Positional args: ('Zia', 'Weise')
# Keyword args: {'toy': 'feather wand', 'snack': 'tuna'}