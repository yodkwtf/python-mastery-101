## Rasing Your Own Errors

- In Python we can also throw our own errors using the **raise** keyword.
- Helpful when creating your own kinds of exception and error messages

```py
raise ValueError('invalid value')
# throws a value error
```

- We have to be raise errors in a decent way with errors that make sense.

---

## Try and Catch Blocks

- In python we should use try/except block to handle errors and do something about them

```py
foobar # NameError (since it makes no sense as it isn't defined)

# using try/except blocks
try:
  foobar
except:
  print("There's a problem") # "There's a problem" (Prints custom msg instead of throwing a NameError)
```

- Even though we can do it, we should not catch every single error because then we would not be able to identify what went wrong with our code.

- We can try to be more specific about the type of error in except block and that way it will only catch a certain type of error
  ```py
  try:
    foobar
  except NameError:
    print("There's a problem")
  ```
