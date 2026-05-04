# empty tuples
empty_tuple = ()
print(empty_tuple)
# tuples with values
my_tuple = (1, 2, 3, 'hello', [4, 5], (6, 7))
print(my_tuple)
# accessing tuple elements
print(my_tuple[0])  # first element
print(my_tuple[3])  # 'hello'
print(my_tuple[4])  # [4, 5]
print(my_tuple[5])  # (6, 7)

# tuples are immutable, so we cannot change their elements
# my_tuple[0] = 10  # This will raise a TypeError   

# tuples unpacking
cat_info =('Whiskers', 3, 'Siamese')
name,age,breed = cat_info
print(f"Name: {name}, Age: {age}, Breed: {breed}")

