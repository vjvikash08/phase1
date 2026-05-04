# WHILE LOOP
count =0
while count <5:
    print(count)
    count +=1
# ---------------------
# secret_word = "python123"
# attempt=""
# while attempt !=secret_word:
#     attempt= input("guess the word:")
# print("You've guessed it right!")

# ----------FOR LOOP--------------
baskets_toys =["feather","ball","laser pointer"]
for toy in baskets_toys:
    print("Checking:",toy)
    
# -------------------------------
for i in range(5):
    print(i)
# 0 1 2 3 4

for i in range(1,6):
    print("Number",i)
    # 1 2 3 4 5 
for i in range(2,10,2):
    print(i)
    # 2,4,6,8

# -------Looping over collections-----------
cat_toys = ['feather','ball','laser pointer','scratching pads']
for toy in cat_toys:
    print("_",toy)

# Loop over a tuple --------------
coordinates=(10,20,30)
for coordinate in coordinates:
    print(coordinate)
    
# Loop over a dictionary --------------
car_attributes ={
    "name":"Zia",
    "age":1,
    "color":"grey",
}

for key in car_attributes:
    print(key,":",car_attributes[key])
    
for value in car_attributes.values():
    print(value)
    
for key,value in car_attributes.items():
    print(f"- {key} : {value}")
    
# --------Nested Loop-----------------
for i in range(1,4):
    for j in range(1,4):
        product = i*j
        print(f"{i} * {j} ={product}")
    print("---")

# ----iterating a list of lists-------
list_of_lists = [
    ["weise","Pino","Hedgehog"],
    ["Zia","Python","Writing"]
]

for inner_list in list_of_lists:
    for item in inner_list:
        print(item)
        
# break and continue 
for number in range(1,10):
    if number == 5:
        print("found 5! Stopping")
        break
    print("Number",number)
print("Loop ended")

# -------------------------
# while True:
#     text = input("Stop? ")
#     if text == "yes":
#         break
# continue - skip to next iteration 
for number in range(1,6):
    if number == 3:
        print("Skipping 3......")
        continue
    print("Number",number)
    
# =============FOR ELSE =============
toys = ["ball","mouse","string"]
for toy in toys:
    if toy == "feather":
        print("Found feather!")
        break
else:
    print("No feather found - nap time")
# ==============
toys= ["ball","feather",'string']

for toy in toys:
    if toy == "feather":
        print("feather found")
    break
else:
    print("No feather found - nap time")
# ====================================
# MODIFYING A LIST WHILE LOOPING OVER IT
# -----------------------------------
toys = ["ball","feather"]
for item in toys:
    toys.append("new toy")
# adding to a list while looping creates an infinte loop:

#Removing while looping can skip elements:
numbers =[1,2,3,4,5]
for num in numbers:
    if num ==2 :
        numbers.remove(num)
print(numbers)