def is_isogram(string):
    s = set(string.lower())
    return True if len(s) == len(string) else False


print(is_isogram('Qqwertyui'))
