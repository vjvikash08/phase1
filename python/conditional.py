hour = 18
if hour == 18:
    print("Time to go home!")

a = 5
b = 3
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")

zia_weight = 2.2
wiese_weight = 1.8
if zia_weight > wiese_weight:
    print("Zia is heavier than Wiese")

# else statements
# if condition:
#     # runs this code
#     pass
# else:  # run this code instead
#     print("Condition is false")

# ---------------------------------
# is_hungry = True

# if is_hungry:
#     print("Time to eat!")
# else:
#     print("Not hungry right now.")

# # the elif statement
# if condition1:
#     # runs this code
#     pass
# elif condition2:
#     # runs this code instead
#     pass
# else:  # runs this code if both condition1 and condition2 are false
#     pass
# --------------------------------
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
elif weather == "rainy":
    print("Take an umbrella!")
elif weather == "snowy":
    print("Wear a coat!")
else:
    print("Have a nice day!")
# nested elseif statements

is_awake = True
has_toy = False

if is_awake:
    if has_toy:
        print("Play with the toy!")
    else:
        print("Find a toy to play with!")
else:
    print("Go to sleep!")
# Or - at least one condition must be true
id_bored = True
is_tired = False
if id_bored or is_tired:
    print("Take a break!")
else:
    print("Keep working!")

# ----------------------------------------
# not - inverts a boolean
is_raining = False
if not is_raining:
    print("It's not raining, enjoy the weather!")

# Flattening nested conditionals
if is_awake:
    if has_toy:
        print("Let's play with the toy!")

# Flattened version
if is_awake and has_toy:
    print("Let's play with the toy!")
# ----------------------------------------
# match statement - similar to switch statements in other languages

# match variable:
#     case value1:
#         # runs this code if variable == value1
#         pass
#     case _:
#         # runs this code if variable == value2
#         pass
#     case _:
#         # irrefutable pattern must be last - runs this code if variable doesn't match any of the above cases
#         pass

command = "sit"

match command:
    case "sit":
        print("The dog sits down.")
    case "stay":
        print("The dog stays in place.")
    case "fetch":
        print("The dog fetches the ball.")
    case _:
        print("Unknown command.")
# ----------------------------------------
# ternary operator - a one-line if-else statement
# value_if_true if condition else value_if_false
hour = 14
activity = "No Gap" if hour <12 else "Gap"
print(activity)     
# Output: No Gap
# -----------------------------------------
if hour <17:
    print("Good afternoon!")
else:
    print("Good evening!")
    
# ------------------------------------
if a==5:
    print("a is 5")
    