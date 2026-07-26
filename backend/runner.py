def run_code(lang, code):
    if lang == "Python":
        return False, "Python execution handled in frontend."
    elif lang == "C++":
        return False, "C++ execution backend not implemented yet."
    elif lang == "JavaScript":
        return False, "JavaScript execution backend not implemented yet."
    else:
        return False, "Unknown language."
