#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file:"""

import sys
import os
import json

if __name__ == "__main__":
    filename = "add_item.json"
    
    try:
        with open(filename, 'r') as file:
            loadFile = json.load(file)
    except FileNotFoundError:
        loadFile = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        loadFile.append(sys.argv[idx])

    with open(filename, 'w') as file:
        json.dump(loadFile, file)
