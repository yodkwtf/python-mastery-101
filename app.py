def calculate(**kwargs):
    possible_values = {
        'add': kwargs.get('first') + kwargs.get('second'),
        'subtract': kwargs.get('first') - kwargs.get('second'),
        'multiply': kwargs.get('first') * kwargs.get('second'),
        'divide': kwargs.get('first') / kwargs.get('second')
    }
    
    result = possible_values[kwargs.get('operation')]
    
    if kwargs.get('make_float') == True:
        result = float(result)
    else:
        result = int(result)
        
    if kwargs.get('message'):
        return "{} {}".format(kwargs['message'], result)
    
    return "The result is {}".format(result)

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))