from imp_lexer import *


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


def match(tokens, token):
    if tokens[0][1] == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0][1]))

def parse_e3(tokens):

    if tokens[0][1] == "T_STR":
        return tokens.pop(0)

    match(tokens, "T_LPAR")
    expression = parse_e(tokens)
    match(tokens, "T_RPAR")

    return expression

def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0][1] in ["T_OR", "T_AND"]:
        node = Node(tokens[0][1], value=tokens[0][0])
        tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0][1] in ["T_EQ",
                           "T_UNEQ",
                           "T_MORE",
                           "T_LESS",
                           "T_MORE_EQ",
                           "T_LESS_EQ"
                           ]:
        node = Node(tokens[0][1], value=tokens[0][0])
        tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node


def parse(inputstring):
    tokens = imp_lex(inputstring)
    ast = parse_e(tokens)
    match(tokens, 'T_END')
    return ast



# ast = parse("((name <= “C”) OR (name >= “X”)) OR (name = “Petya”)")
# print(ast.value)
# print(ast.children[1].value)
# print(ast.children[1].children)






