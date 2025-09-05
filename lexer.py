import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+'),
    ('STRING', r'"[^"]*"'),
    ('ID', r'[A-Za-z_]\w*'),
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMI', r';'),
    ('COMMA', r','),
    ('FUNCTION', r'function'),
    ('RETURN', r'return'),
    ('PRINT', r'print'),
    ('SKIP', r'[ \t\n]+'),
    ('MISMATCH', r'.'),
]

def tokenize(code):
    tokens = []
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected token: {value}')
        tokens.append((kind, value))
    return tokens
