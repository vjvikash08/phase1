my_list =[]
list_with_values = [1, 2, 3, 4, 5]
cat_toys =["bail","feather", "mouse"]
print(cat_toys) 
# ['bail', 'feather', 'mouse']
# Append method -add to the end of the list 
cat_toys.append("ball")
print(cat_toys)
# ['bail', 'feather', 'mouse', 'ball']

# Insert method - add to a specific index in the list
# insert(index, value) - insert value at specific index, shifting everything right of it to the right
cat_toys.insert(1, "string")
print(cat_toys)
# ['bail', 'string', 'feather', 'mouse', 'ball']

# REMOVING ITEMS FROM A LIST
# remove(value) - removes the first occurrence of value in the list
cat_toys.remove("ball")
print(cat_toys)
# ['bail', 'string', 'feather', 'mouse']

# pop(index) - remove item at index and return it, if no index is provided,
# it removes and returns the last iten in the list  

# changing an item in a list 
cat_toys[0] = "cat word"
print(cat_toys)


# sclicing a list - get a subset
cat_toys = ["feather","string","mouse","ball"]
favorite = cat_toys[1:4]
# items at index 1 2 3 but not 4


