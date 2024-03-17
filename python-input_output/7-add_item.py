#!/usr/bin/python3
"""Adds all arguments to a Python list, and then saves them to a file."""

import sys
import json
import os

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        with open(filename, 'r') as file:
            load_file = json.load(file)
    except FileNotFoundError:
        load_file = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        load_file.append(sys.argv[idx])

    with open(filename, 'w') as file:
        json.dump(load_file, file)
