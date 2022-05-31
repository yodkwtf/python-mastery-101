## `raise` Your Own Errors

- In Python we can also throw our own errors using the **raise** keyword.
- Helpful when creating your own kinds of exception and error messages

```py
raise ValueError('invalid value')
# throws a value error
```

- We have to raise errors in a decent way with errors that make sense.

---

## `try/except` Blocks

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

#### try, except, else, and finally

**try** - attempts to do something
**except** - runs if there's an error in `try` block
**else** - runs if except doesn't run
**finally** - runs at the end no matter what

```py
try:
  num = int(input("Enter a num")) # runs first
except:
  print("That's not a number") # runs if user enter something other than a number
else:
  print("Nice number, I'll do it") # runs if a number is entered
finally:
  print("Programs ends") # runs at the end anyway
```

- try and except are the ones used the most
- multiple errors can be combined inside a tuple to be handled in a single _except_ block
- we can also give a name to error and handle it inside the except block

  ```py
  try:
    ....
  except TypeError as err:
    print(err)
  ```

---

## Python Debugger - Debugging with PDB

- Used to handle the errors that are not intentional, i.e, we didn't raise it, we didn't expect it
- Handles errors whether it's a huge shouting error or a tiny unexpected bug that isn't even breaking our code
- `pdb` is a module that we import and we a single method to pause the execution of our code
- We can set breakpoints in our code anywhere we want just by inserting this line
  ```
  import pdb; pdb.set_trace()
  ```

When python encounters this line it pauses. It doesn't quit, it doesn't skip everything else, it just pauses and then we can check things out line by line or in our terminal.

#### PDB Gotcha

If you have code with variables names that match the _commands of PDB_ then there may be unexpected results while accessing them in the terminal.

```py
def add_numbers(a,b,c):
  import pdb; pdb.set_trace()

  return a+b+c

add_numbers(1, 2, 3)
```

_In the above example_, if we have a variable called _c_. When we type _c_ in terminal to access it, we will accidentally hit the _continue_ command of pdb instead. In such case we use _p_ command to access the variable.

```bash
p c
```
