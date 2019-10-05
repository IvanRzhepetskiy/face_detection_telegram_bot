#temporary file while we don't have a db plan

import json

def readfile(path):
    try:
        with open(path, "r") as f:
            parcedjson = json.load(f)
            return parcedjson
    except FileNotFoundError as e:
        print(e)

def writefile(path, key, content:list):
    parcedjson = readfile(path)
    parcedjson[key] = content
    with open(path, "w") as f:
        json.dump(parcedjson, f, indent=2)