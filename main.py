from lexer import tokenize
from parser import parse
from semantic import analyze
from codegen import generate_code
from interpreter import interpret
from assemblygen import generate_assembly

def run_code(source_code):
    tokens = tokenize(source_code)
    ast = parse(tokens)
    analyze(ast)
    code = generate_code(ast)
    result = interpret(code)
    asm = generate_assembly(ast)
    return f"Environment: {result}\nAssembly:\n{asm}"

if __name__ == "__main__":
    src = '''
    function add(a, b) {
        return a + b;
    }
    x = add(3, 4);
    print x;
    '''
    print(run_code(src))
