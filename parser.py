def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'FUNCTION':
            name = tokens[i+1][1]
            args = []
            i += 3  # skip FUNCTION name (
            while tokens[i][0] != 'RPAREN':
                if tokens[i][0] == 'ID':
                    args.append(tokens[i][1])
                i += 1
            i += 2  # skip ) {
            body = []
            while tokens[i][0] != 'RBRACE':
                body.append(tokens[i])
                i += 1
            ast.append(('function', name, args, body))
            i += 1
        elif token[0] == 'ID' and tokens[i+1][0] == 'ASSIGN':
            ast.append(('assign', token[1], tokens[i+2][1]))
            i += 4
        elif token[0] == 'PRINT':
            ast.append(('print', tokens[i+1][1]))
            i += 3
        elif token[0] == 'ID' and tokens[i+1][0] == 'LPAREN':
            name = token[1]
            args = []
            i += 2
            while tokens[i][0] != 'RPAREN':
                if tokens[i][0] in ('ID', 'NUMBER', 'STRING'):
                    args.append(tokens[i][1])
                i += 1
            ast.append(('call', name, args))
            i += 2
        elif tokens[i][0] == 'RETURN':
            body.append(('RETURN', tokens[i+1][1]))
            i += 3  # skip RETURN value SEMI
        else:
            i += 1
    return ast
