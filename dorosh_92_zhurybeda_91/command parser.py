from imp_lexer import *
import re
"""тут все может(скорее всего будут по другому)"""
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def parse_command(command: str):
    parts = imp_lex(command)
    for val, tag in parts:
        if tag == COM_NAME:
            com_name = val
    if com_name.lower() == "create":
        table_name = parts[i][0]
        for i in range(len(parts)):
            if parts[i][1] == "NAME":
    return com_name, table_name



print(parse_command("CREATE cats (id INDEXED, name INDEXED, favourite_food)"))

string = imp_lex("CREATE cats (id INDEXED, name INDEXED, favourite_food)")
print(string)



