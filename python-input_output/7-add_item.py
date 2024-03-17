#!/usr/bin/python3
"""Adds all arguments to a Python list, and then saves them to a file."""

import sys
import json
from os.path import exists
from importlib import import_module

if __name__ == "__main__":
    save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
    load_from_json_file = import_module('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        load_file = load_from_json_file(filename)
    except FileNotFoundError:
        load_file = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        load_file.append(sys.argv[idx])

    save_to_json_file(load_file, filename)
