import json

def get_config():
    with open("config/config.json") as file:
        return json.load(file)