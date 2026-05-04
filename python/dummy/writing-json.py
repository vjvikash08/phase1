import json 

data ={
    "pet":"Zia",
    "toys":["feather wand","ball","laser pointer"],
    "weight":2.2
}

with open("dummy.json", "w") as f:
    json.dump(data,f)