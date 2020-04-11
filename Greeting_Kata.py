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
        upperName = ''
        sepNames = []
        for n in name:
            if n.isupper():
                upperName = n
                name.remove(n)
            if n.find('\"') != -1:
                newString = n.replace('\"', '')
                name.remove(n)
                name.append(newString)
            elif n.find(',') != -1:
                sepNames = n.split(', ')
                name.remove(n)
                for s in sepNames:
                    name.append(s)
        for i in range(len(name)):
            if i == len(name)-1:
                string = string + 'and ' + name[i]
            elif len(name) < 3 and i != len(name)-1:
                string = string + name[i] + ' '
            else:
                string = string + name[i] + ', '
        string = string + '.'
        if upperName is not '':
            string = string + ' AND HELLO ' + upperName + '!'
    return string