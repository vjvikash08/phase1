import csv

with open("pets.csv","a",newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["Muchu","Cat","0"])    