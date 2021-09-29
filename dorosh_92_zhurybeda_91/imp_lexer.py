import lexer

RESERVED = 'RESERVED'
NAME = 'NAME'
COM_NAME = 'COM_NAME'
COL_VALUE = 'COL_VALUE'
OP = 'OP'
SPEC_WORD = "SPEC_WORD"

token_exprs = [
    (r'[\s\n\t]+', None),
    # (r'#[^\n]*', None),
    (r',', RESERVED),
    # (r'“', RESERVED),
    # (r'”', RESERVED),
    (r'\(', RESERVED),
    (r'\)', RESERVED),
    (r'\*', RESERVED),
    (r'<=', OP),
    (r'<', OP),
    (r'>=', OP),
    (r'>', OP),
    (r'=', OP),
    (r'!=', OP),
    (r'and|AND', RESERVED),
    (r'or|OR', RESERVED),
    (r'\|', RESERVED),
    (r'CREATE|create', COM_NAME),
    (r'INDEXED|indexed', SPEC_WORD),
    (r'INSERT|insert', COM_NAME),
    (r'INTO|into', SPEC_WORD),
    (r'DELETE|delete', COM_NAME),
    (r'SELECT|select', COM_NAME),
    (r'FROM|from', SPEC_WORD),
    (r'WHERE|where', SPEC_WORD),
    (r'[A-z\d]+', NAME),
    (r'“[A-z\d\s]+”', COL_VALUE)

]

def imp_lex(characters):
    return lexer.lex(characters, token_exprs)

print(imp_lex("(name<=“Murzik”)OR(name=“Pushok”)"))