def hello(name):
    return 'hello ' + name
print(hello('Theodore'))


def str_len(str = 'None'):
    if str == 'None':
        return str
    else:
        return len(str)
print(str_len("lorem"))
print(str_len())


# return ინახავს მაგრამ არ პრინტავს და print ინახავს და პრინტავს პირდაპირ.