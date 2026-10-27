import re

def check(regex, name):
    match = re.search(regex, name)
    if match: return match.group(0) == name
    return False

print(check(input("? "), "test"))
