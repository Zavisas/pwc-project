def remove_repeated(key):
    return "".join(list(dict.fromkeys(key.upper())))
print(remove_repeated('Hello, World!'))