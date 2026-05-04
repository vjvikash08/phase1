import json

with open("dummy.json","r") as file:
    loaded = json.load(file)
    print(loaded["pet"])
    print(loaded["toys"][0])