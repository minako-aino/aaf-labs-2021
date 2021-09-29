import enum
import re
import sys


class TokenType(enum.Enum):
    T_STR = 0
    T_EQ = 1
    T_UNEQ = 2
    T_MORE = 3
    T_LESS = 4
    T_MORE_EQ = 5
    T_LESS_EQ = 6
    T_OR = 7
    T_AND = 8
    T_LPAR = 9
    T_RPAR = 10
    T_END = 11


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


# def lexical_analysis(s):
#     mappings = {
#         r'=': TokenType.T_EQ,
#         r'!=': TokenType.T_UNEQ,
#         r'>': TokenType.T_MORE,
#         r'<': TokenType.T_LESS,
#         r'>=': TokenType.T_MORE_EQ,
#         r'<=': TokenType.T_LESS_EQ,
#         r'OR': TokenType.T_OR,
#         r'AND': TokenType.T_AND,
#         r'(': TokenType.T_LPAR,
#         r')': TokenType.T_RPAR}
#
#     tokens = []
#     for c in s:
#         if c in mappings:
#             token_type = mappings[c]
#             token = Node(token_type, value=c)
#         elif re.match(r'[A-z“”]+', c):
#             token = Node(TokenType.T_STR, value=str(c))
#         else:
#             raise Exception('Invalid token: {}'.format(c))
#         tokens.append(token)
#     tokens.append(Node(TokenType.T_END))
#     return tokens

def lexical_analysis(characters):
    token_exprs = {
        (r'\(', TokenType.T_LPAR),
        (r'\)', TokenType.T_RPAR),
        (r'>=', TokenType.T_MORE_EQ),
        (r'>', TokenType.T_MORE),
        (r'<=', TokenType.T_LESS_EQ),
        (r'<', TokenType.T_LESS),
        (r'!=', TokenType.T_UNEQ),
        (r'=', TokenType.T_EQ),
        (r'OR', TokenType.T_OR),
        (r'AND', TokenType.T_AND),
        (r'[A-z“”]+', TokenType.T_STR)}

    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = Node(tag, value=text)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    tokens.append(Node(TokenType.T_END))
    return tokens


def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0].token_type in [TokenType.T_EQ,
                                   TokenType.T_UNEQ,
                                   TokenType.T_MORE,
                                   TokenType.T_LESS,
                                   TokenType.T_MORE_EQ,
                                   TokenType.T_LESS_EQ
                                   ]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node


def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0].token_type in [TokenType.T_OR, TokenType.T_AND]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e3(tokens):
    if tokens[0].token_type == TokenType.T_STR:
        return tokens.pop(0)

    match(tokens, TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)

    return expression


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast


tokens = lexical_analysis("(name<=“Murzik”)OR(name=“Pushok”)")
for token in tokens:
    print(token.value, token.token_type)
# parse_e3(expr)
