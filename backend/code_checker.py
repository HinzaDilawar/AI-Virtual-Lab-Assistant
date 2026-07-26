import ast

def check_code(user_code):
    """
    Returns a consistent 4-tuple: (is_valid, message, hint, solution)
    """
    try:
        ast.parse(user_code)
        return True, "Code syntax is correct!", "", ""
    except SyntaxError as e:
        line = e.lineno
        msg = e.msg
        hint = f"Check syntax near line {line}"
        solution = f"Fix the syntax error on line {line}: {msg}"
        return False, f"SyntaxError at line {line}: {msg}", hint, solution
    except Exception as e:
        return False, str(e), "Unexpected error", "Review your code carefully"

