import json
import time

days = ["Monday","Tuesday","Wednesday","Thursday","Friady"]

#Import the config.json file
with open('config.json','r') as json_file:
    data = json.load(json_file)

print(data["names"][1].value())