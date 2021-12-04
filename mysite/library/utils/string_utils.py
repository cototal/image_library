import re

def parameterize(string):
    return re.sub(r'[ \(\)\[\]!@#$%^&*+=?\.\/\-]+', '-', string.lower())
