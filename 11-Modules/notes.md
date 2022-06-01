## Why use Modules?

- keeps python files small
- reuse code across multiple files
- a module is just a python file

## Built-In Modules

- comes with python by default
- we import them to our file to use it
- there are a ton of them, refer to docs

```py
import random

random.choice(['apple', 'banana', 'melon']) # picks out a random value
```

- we can give the module an alias

```py
import random as ran

ran.randint(1, 100) # picks a random no. b/w 1-100
```

- we can also import just parts of a module

```py
from random import randint

randint(1, 100) # picks a random no. b/w 1-100
```

> Try to only import the methods you actually need instead of importing the whole module

## Custom Modules

- just a python file we created that we can import into other files

- let's say we have a file called `file1.py` with the following code

```py
def fn():
  print('hello friend')

def fn1():
  print('Good Morning Sir')
```

- Now let's say we need to use the above functions in another file `file2.py`

```py
import file1

file1.fn() # prints 'hello friend'
```

- They do need to be in the same directory otherwise we'd need to provide proper paths

#### \_\_name\_\_ variable

- every python file has \_\_name\_\_ variable
- it's value is the name of the file unless it's the primary file (something like app.py)
- for primary files , it's value is \_\_main\_\_

> when import finds a file it runs the code inside that file which can sometimes result in extra print statements

we can prevent the above issue by using a condition where the code should only execute if name variable is eq to main

## External Modules

- modules created by python devs all around the world
- external modules are downloaded using **pip**

```bash
python3 -m pip install NAME_OF_PACKAGE
```

#### autopep8

- Formats code based on the autopep style guide

```bash
autopep8 -i file_name.py
```

- there are more options like `-i` & `-a`
