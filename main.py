def collapse_spaces(text):
    result = []
    for char in text:
        if char == " ":
            if len(result) > 0 and result[-1] == " ":
                result.pop()
                continue
        result.append(char)
    return "".join(result)