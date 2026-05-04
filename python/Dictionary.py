# empty dictionary 
my_dict = {}
print(my_dict)

# Dictionary with items 
car_attributes={
    "name":"Zia",
    "age":1,
    "color":"grey",
    "favorite_food":"milk"
}

# accessing items
print(car_attributes["name"])
print(car_attributes["age"])
print(car_attributes["color"])
print(car_attributes["favorite_food"])

# Returns none if missing key is accessed
breed = car_attributes.get("breed")
print(breed) 
# None

# Modifying Dictionary
car_attributes["hobby"] = "playing with toys"
print(car_attributes)

# updating existing key
car_attributes["age"] = 2
print(car_attributes)

# Removing entries
del car_attributes["hobby"]
print(car_attributes)

removed_value = car_attributes.pop("color")
print(removed_value) # grey
print(car_attributes) # {'name': 'Zia', 'age': 2, 'favorite_food': 'milk'}

# DICTIONARY METHODS
# keys() method
keys = car_attributes.keys()
print(keys) # dict_keys(['name', 'age', 'favorite_food'])
# values() method
values = car_attributes.values()
print(values) # dict_values(['Zia', 2, 'milk'])
# items() method
items = car_attributes.items()
print(items) # dict_items([('name', 'Zia'), ('age', 2), ('favorite_food', 'milk')])

# combining/nesting dictionaries
car_attributes={
    "name":"Zia",
    "hobbies": ["playing with toys", "chasing laser pointer"],
}

# Accessing nested dictionary
print(car_attributes['hobbies']) # ['playing with toys', 'chasing laser pointer']
print(car_attributes['hobbies'][0]) # playing with toys

# Dictionary inside a list 
cat_att={
    "name":"Zia",
    "friends":[
        {"name":"Wiesey", "age":3,"hobbies":["napping", "eating"]},
        {"name":"Mia", "age":2,"hobbies":["playing with toys", "chasing laser pointer"]}
    ]
}

# get the name of the first friend
first_friend_name = cat_att["friends"][0]["name"]
second_friend_hobbies = cat_att["friends"][1]["hobbies"]
print(first_friend_name) # Wiesey
print(second_friend_hobbies) # ['playing with toys', 'chasing laser pointer']