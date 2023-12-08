import re

def get_nums(s):
    return re.findall(r"\\d+", s)
