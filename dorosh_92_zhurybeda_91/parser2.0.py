import re
from cond_parser_tuple import *
from imp_lexer import *

token_exprs = [
    (r'[\s\n\t\r]+', None),
    # (r'#[^\n]*', None),
    (r'(?i)create', "T_CREATE"),
    (r'(?i)delete', "T_DELETE"),
    (r'(?i)insert', "T_INSERT"),
    (r'(?i)select', "T_SELECT"),
    (r'((?i)into)|((?i)from)', None),
    (r'(?i)INDEXED', "T_INDEXED"),
    (r',', "T_SEP"),
    (r'\(', 'T_LPAR'),
    (r'\)', "T_RPAR"),
    (r'[A-z\d\"_]+', "T_STR"),
    (r'\*', "T_ALL"),
    (None, "T_END")
]


def parse_create(tokens):
    if tokens[0][1] == "T_CREATE":
        com_name = tokens.pop(0)
        table_name = tokens.pop(0)
        match(tokens, "T_LPAR")
        col_name = {}
        for i in range(len(tokens)):
            if tokens[i][1] == "T_STR":
                if tokens[i + 1][1] == "T_INDEXED":
                    col_name[tokens[i][0]] = 1
                else:
                    col_name[tokens[i][0]] = 0
        if tokens[-2][1] != "T_RPAR" or tokens[-1][1] != "T_END":
            print("syntx error")
            return None
        return com_name, table_name, col_name


# com = imp_lex("CREATE cats (id INDEXED, name INDEXED, favourite_food)")
# print(com)
# print(parse_create(com))

def parse_insert(tokens):
    if tokens[0][1] == "T_INSERT":
        com_name = tokens.pop(0)
        table_name = tokens.pop(0)
        match(tokens, "T_LPAR")
        col_name = []
        for i in range(len(tokens)):
            if tokens[i][1] == "T_VALUE":
                val = tokens[i][0]
                col_name.append(val)
            if tokens[-2][1] != "T_RPAR" or tokens[-1][1] != "T_END":
                print("syntx error")
        return com_name, table_name, col_name


# com = imp_lex('INSERT INTO cats ("1", "Murzik", "Sausages")')
# print(parse_insert(com))

def parse_select(tokens):
    col_name = []
    cond = None
    if tokens[0][1] == "T_SELECT":
        com_name = tokens[0][1]
        for i in range(len(tokens)):
            if tokens[i][1] == "T_WHERE":
                icond = i
        if icond:
            for i in range(icond):
                if tokens[i][1] == "T_ALL" or tokens[i][1] == "T_STR":
                    col_name.append(tokens[i][0])
            cond = parse(tokens[icond + 1:])
            tab_name = col_name.pop(-1)
            return com_name,tab_name, col_name,  cond
        else:
            for i in range(len(tokens)):
                if tokens[i][1] == "T_ALL" or tokens[i][1] == "T_STR":
                    col_name.append(tokens[i][0])
            tab_name = col_name.pop(-1)
            return com_name, tab_name, col_name

# com1 = imp_lex('SELECT * FROM cats')
# string = imp_lex('SELECT id, favourite_food FROM cats WHERE (name <= "Murzik") OR (name = "Pushok")')
# print(parse_select(string))
# print(parse_select(com1))

com1 = imp_lex('DELETE FROM cats')
com2 = imp_lex('DELETE cats WHERE name = "Murzik"')
com3 = imp_lex('DELETE cats WHERE id != "2"')
print(com1)
print(com2)
print(com3)
def parse_delete(tokens):
    icond = None
    if tokens[0][1] == "T_DELETE":
        com_name = tokens[0][1]
        for i in range(len(tokens)):
            if tokens[i][1] == "T_WHERE":
                icond = i
        if icond:
            tab_name = tokens[icond-1][0]
            cond = parse(tokens[icond+1:])
            return com_name, tab_name, cond
        else:
            for i in range(len(tokens)):
                if tokens[i][1] == "T_STR":
                    tab_name = tokens[i][0]
            return com_name, tab_name

print(parse_delete(com1))
print(parse_delete(com2))
print(parse_delete(com3))

