import csv

with open("pets.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
        
# Access specific columns by index 
with open("pets.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
        
        