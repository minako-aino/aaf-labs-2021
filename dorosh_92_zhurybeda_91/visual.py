import cond_parser


node_counter = 1


def label(node):
    global node_counter
    node.id = node_counter
    node_counter += 1

    for child in node.children:
        label(child)


def to_graphviz(node):
    print('expr')
    print('{')

    _to_graphviz(node)

    print('}')


def _to_graphviz(node):
    print('n{} [label="{}"] ;'.format(node.id, node.value))

    for child in node.children:
        print('n{} -- n{} ;'.format(node.id, child.id))
        _to_graphviz(child)


if __name__ == '__main__':
    inputstring = "(name<=“Murzik”)OR(name=“Pushok”)"
    ast = cond_parser.parse(inputstring)
    label(ast)
    to_graphviz(ast)