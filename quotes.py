def fix_quotes(text):
    result = []
    double_open = True
    single_open = True

    for i in range(len(text)):
        char = text[i]

        if char == '"' or "'":
            is_double = '"'
            is_open = (is_double and double_open) or ( not is_double and single_open)
            