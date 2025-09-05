def generate_code(ast):
    code = []
    for node in ast:
        if node[0] == 'assign':
            code.append(f"{node[1]} = {repr(node[2])}")
        elif node[0] == 'print':
            code.append(f"print({node[1]})")
        elif node[0] == 'call':
            args = ', '.join(node[2])
            code.append(f"{node[1]}({args})")
        elif node[0] == 'function':
            args = ', '.join(node[2])
            body_lines = []
            for tok in node[3]:
                if tok[0] == 'RETURN':
                    body_lines.append(f"    return {tok[1]}")
            code.append(f"def {node[1]}({args}):\n" + '\n'.join(body_lines))
    return code
