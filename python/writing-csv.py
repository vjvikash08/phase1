import csv

with open("pets.csv","w",newline="") as file:
    writer= csv.writer(file)
    writer.writerow(["name","species","Age"])
    writer.writerow(["zia","Cat","1"])
    writer.writerow(["weise","Dog","7"])
    
