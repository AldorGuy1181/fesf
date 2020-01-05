def makebold(fn,something):
    def wrapped():
        return f"<{something}> " + fn() + f"<{something}>"
    return wrapped


@makebold("|")
def get_text(text='I code with PyBites'):
    return text

print(get_text())


#I want the output to be <|>I code with PyBites<|>
#But it keeps saying that i am missing 1 required positional argmuent, even though i 'feel' :D that im declaring it in line 7
