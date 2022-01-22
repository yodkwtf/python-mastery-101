# handling multiple types of errors at once
def divide(a, b):
  try:
    return a/b
  except ZeroDivisionError:
    return "Cannot divide a number by zero"
  except TypeError as err:
    print(err)
    return "Both the arguments should be numbers"

print(divide(10, 5)) # 2.0
print(divide(2, 0)) # Cannot divide a number by zero
print(divide("10", 5)) # Both the arguments should be numbers