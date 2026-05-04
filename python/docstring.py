def area_of_circle(radius):
    """
    Returns the area of a circle with a given radius
    Uses the formula:pi*r^2
    """
    import math
    return math.pi*radius**2

def get_pet_info():
    """
    Asks the user pet info
    returns a tuple (pet_name,species,food)
    """
    pet_name = input("what's your pet's name?")
    if pet_name.lower() == "quit":
        return None
    species = input("Species? ")
    food = input("Food?")
    return (pet_name,species,food)
