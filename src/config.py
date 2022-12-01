import json

def get_config() -> dict:
    with open("config.json") as f:
        read = json.load(f)
        return read
