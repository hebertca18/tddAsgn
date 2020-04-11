def greet(name):
    if name is None:
        name = 'my friend'
    if isinstance(name, str):
        if name.isupper():
            string = 'HELLO ' + name + '!'
        else:
            string = 'Hello, ' + str(name) + '.'
    else:
        string = 'Hello, '
        for i in range(len(name)):
            if i == len(name)-1:
                string += ' and '
            string = string + name[i]
        string = string + '.'
    return string