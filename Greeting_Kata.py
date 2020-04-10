def greet(name):
    if name is None:
        name = 'my friend'
    if name.isupper():
        string = 'HELLO ' + name + '!'
    else:
        string = 'Hello, ' + str(name) + '.'
    return string