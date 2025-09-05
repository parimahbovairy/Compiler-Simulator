def generate_assembly(ast):
    asm = []
    for node in ast:
        if node[0] == 'assign':
            asm.append(f"LOAD R1, {node[2]}")
            asm.append(f"STORE {node[1]}, R1")
        elif node[0] == 'print':
            asm.append(f"PRINT {node[1]}")
        elif node[0] == 'call':
            asm.append(f"CALL {node[1]}")
    return '\n'.join(asm)
