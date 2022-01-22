## Types of Errors

#### SyntaxError

- Occurs when python encounters incorrect syntax
- Usually due to typos

```py
def first: # missing the parenthesis

None = -1 # `None` can't be a variable
```

#### NameError

- occurs when a variable isn't defined or hasn't been assigned a value

```py
print('name') # name

print(name) # NameError: 'name' isn't defined
```

#### TypeError

- mismatch of data types
- occurs when an operation or function is applied to wrong data type

```py
len(5) # TypeError: 'int' has no len()

"awesome" + [] # TypeError: can't concatenate 'str' and 'list'
```

#### IndexError

- occurs when we try to access an element in a list using an invalid index

```py
list1 = ["hey", "hello"]

list1[4] # IndexError: list index out of range
```

#### ValueError

- occurs when a built-in operation or function gets an argument that has the right type but inappropriate value

```py
int('55') # 55 (as an integer)

int("joe") # ValueError: invalid literal for int()
```

#### KeyError

- Occurs when a dictionary does not have a specified key

```py
d = {}

d["foo"] # KeyError: 'foo'
```

#### AttributeError

- Occurs when a variable does not have an attribute

```py
"awesome".foo # AttributeError: 'str' object has no attribute 'foo'

[1,2,3].hello() # AttributeError: 'list' object has no attribute 'hello'
```

---

There are a lot of errors and they can referenced through the python docs. Also whenever you get an error, just google it and it'll be fairly simply to find that error.
