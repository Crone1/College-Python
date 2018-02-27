import sys


def l2d(file):
    dictionary = {}

    lines = file.readlines()

    keys, values = lines[0], lines[1]

    i = 0
    while i < len(keys.strip().split()):
        dictionary[keys.strip().split()[i]] = values.strip().split()[i]
        i = i + 1

    return dictionary
