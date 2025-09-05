def analyze(ast):
    symbol_table = {}
    for node in ast:
        if node[0] == 'assign':
            symbol_table[node[1]] = 'variable'
        elif node[0] == 'function':
            symbol_table[node[1]] = 'function'
    return symbol_table
