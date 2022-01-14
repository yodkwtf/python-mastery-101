## Functions

Block of code that performs similar tasks every time it is run

```py
# defining a function
def name_of_function():
  # all the code
  print('Hi')

# invoking function by calling it
name_of_function() # Hi
```

##### THE `RETURN` KEYWORD

- returns/export a value from a function that can be stored in a variable to use it later
- it exits the function right away and anything below it will be ignored
- it pops the function off the call stack
- we can return anything and not just a single item

```py
def greet_user():
  return 'Hello Sir!'

# getting returned value
greeting = greet_user()
print(greeting) # Hello Sir!
```
