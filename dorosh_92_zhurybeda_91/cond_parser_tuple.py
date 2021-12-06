from imp_lexer import *


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.right = None
        self.left = None


def match(tokens, token):
    if tokens[0][1] == token:
        return tokens.pop(0)[0]
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0][1]))


def parse_e3(tokens):
    if tokens[0][1] in ["T_STR", "T_VALUE"]:
        node = Node(tokens[0][1], value=tokens[0][0])
        tokens.pop(0)[0]
        return node

    match(tokens, "T_LPAR")
    expression = parse_e(tokens)
    match(tokens, "T_RPAR")

    return expression


def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0][1] in ["T_OR", "T_AND"]:
        node = Node(tokens[0][1], value=tokens[0][0])
        tokens.pop(0)[1]
        node.left = left_node
        node.right = parse_e3(tokens)
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
        tokens.pop(0)[0]
        node.left = left_node
        node.right = parse_e2(tokens)
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


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.value),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)
# com = imp_lex('((name <= "C") OR (name >= "X"))')
# ast = parse(com)
# print(ast)

# com = imp_lex('(name <= "Murzik") OR (name = "Pushok") AND (dog = "Shiba")')
# ast = parse(com)
# print(ast)
# printPreorder(ast)
# print(ast.children[0].value)
# print(ast.children[0].children[0])
# print(ast.children[0].children[1])
