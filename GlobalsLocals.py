name = 'hi'

def loc():
    name = 'hello'
    print(globals()['name'])


loc()
