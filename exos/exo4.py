def remove_duplicates(source):
    output = []
    for char in source:
        if char not in output:
            output.append(char)
    return output
