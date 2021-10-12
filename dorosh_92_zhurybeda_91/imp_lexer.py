import lexer


token_exprs = [
    (r'[\s\n\t]+', None),
    # (r'#[^\n]*', None),
    (r'\(', 'T_LPAR'),
    (r'\)', "T_RPAR"),
    (r'<=', "T_LESS_EQ"),
    (r'<', "T_LESS"),
    (r'>=', "T_MORE_EQ"),
    (r'>', "T_MORE"),
    (r'=', "T_EQ"),
    (r'!=', "T_ENEQ"),
    (r'and|AND', "T_AND"),
    (r'or|OR', "T_OR"),
    (r'\|', "T_OR"),
    # (r'[A-z\d]+', "NAME"),
    (r'[A-z\d\s“”]+', "T_STR"),
    (None, "T_END")
    ]

def imp_lex(characters):
    tokens = lexer.lex(characters, token_exprs)
    tokens.append((None, "T_END"))
    return tokens

# tokens = imp_lex('(name <= “Murzik”) OR (name = “Pushok”)')
#
# print(tokens)
