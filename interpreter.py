def interpret(code):
    env = {}
    for line in code:
        try:
            exec(line, {}, env)
        except Exception as e:
            print(f"Error: {e}")
    return env
