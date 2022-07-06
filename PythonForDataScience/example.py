def decision(text):
    length = len(text)
    if length > 17:
        return "This is a long string " + str(length)
    else:
        return "This is a short string " + str(length)


print(decision("salut les zeros "))
