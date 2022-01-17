"""
#QUESTION
- Oh boy, this is a complicated set of instructions. Bear with me. Write a function called calculate that accepts a list of keyword arguments 
• make_float , a boolean which returns a float if True or an integer if False. 
• operation which is either 'add', 'subtract', 'multiply', and 'divide'. 
• first which is a number, second , which is another number, and message which is a string that can be added.

- The function should return the result of actually running the specified operation with the first and second keyword arguments. 

- The result of the operation with the first and second is an integer if the make_float keyword argument is False , otherwise the result of the operation is a float. 

- If a message is specified, it should return the message keyword argument + the result of the operation. Otherwise, it should return the string "The result is " joined with the result of the operation. 
"""

## ANSWER 

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

## TESTS 
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))