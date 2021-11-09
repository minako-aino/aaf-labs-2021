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
    if tokens[0][1] in ["T_STR", "T_VALUE"]:
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


def parse(tokens):
    ast = parse_e(tokens)
    match(tokens, 'T_END')
    return ast


# TODO create cond print
def _print_ast(ast):
    if type(ast) is Node:
        print(ast.value + ' ')
        _print_ast(ast.children[1])
        _print_ast(ast.children[0])
    elif type(ast) is list:
        print(ast[0])
        print(ast[1])


def print_ast(ast):
    if ast.value is not None:
        _print_ast(ast.value)


com = imp_lex('((name <= "C") OR (name >= "X"))')
ast = parse(com)
# print(type(ast) == Node)
# print_ast(ast)
# ast = parse('(name <= "Murzik") Or (name = "Pushok")')
print(ast.value)
print(ast.children[0].value)
print(ast.children[0].children[0])
print(ast.children[0].children[1])
