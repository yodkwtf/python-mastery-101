## Dictionaries

- Are used to describe data in more detail
- Data structure that consists key-value pairs
- `keys` are used to describe data and `values` are used to represent data
- `keys` are usually num or strings but `values` can be anything from boolean to nested dictionaries
- There is no fixed order for items in a dictionary, they are unordered

---

## Accessing Individual Values

```bash
# creating a dictionary
cat = {
  "name": "Kitty",
  "age" : 5,
  "isCute": True
}

# accessing properties
cat["name"] # Kitty
```

---

## Iterating Over Dictionaries

- use `for v in dict.values()` to iterate over values
- use `for k in dict.keys()` to iterate over keys
- use `for k,v in dict.items()` to iterate over both at the same time

---

## Using `In` with Dictionaries

```bash
cat = {
  "name": "Kitty",
  "age" : 5,
  "isCute": True
}

###### DOES A DICTIONARY HAVE A KEY?
print("name" in cat) # True
print("nails" in cat) # False

###### DOES A DICTIONARY HAVE A VALUE?
print("Kitty" in cat.values()) # True
print("Pussy" in cat.values()) # False

# ! THE BELOW CODE WILL THROW AN ERROR
if cat["nails"]:
  print("nail")

# ! THE CORRECT WAY
if "nails" in cat:
  print("nail)
```

---

## Dictionary Methods

##### clear()

- empty out the dictionary

  ```bash
    d = dict(a=1,b=2)
    print(d ) # {'a':1, 'b':2}
    d.clear()
    print(d) # {}
  ```

##### copy()

- copies one dictionary to another variable but they don't point to the same in memory

  ```bash
  d = dict(a=1,b=2)
  c = d.copy()
  print(c) # {'a':1, 'b':2}
  print(c == d) # True
  print(c is d) # False
  ```

##### fromkeys()

- used to dynamically add items to an empty dictionary
- used to set default values

  ```bash
  # add a fixed 'unknown' value to all the keys for new user
  new_user = {}.fromkeys(['name', 'age', 'score'], 'unknown')

  print(new_user) # {'name': 'unknown', 'age': 'unknown', 'score': 'unknown'}
  ```

- if you don't put a list as the first argument and maybe put a string instead then it will iterate over the characters of the strings

- can also use range as an iterable object here
  ```
  new_dict = {}.fromkeys(range(1,10), 'None')
  ```

##### get()

- if we have the specified key, we get its value otherwise we get `None`

  ```bash
  d = dict(a=1,b=2)

  # NORMAL WAY
  print(d['a']) # 1
  print(d['c']) # KeyError

  # USING GET METHOD
  print(d.get('a')) # 1
  print(d.get('c')) # None
  ```

##### pop(key)

- removes the specified key and its value
- gives an error if the key doesn't exist
- returns the value of the item that is removed

  ```bash
  d = dict(a=1,b=2)

  print(d) # {'a':1, 'b':2}
  print(d.pop('a')) # 1
  print(d) # {'b': 2}
  ```

##### popitem()

- removes any random key from the the dictionary
- does not take any argument

##### update()

- add everything from one dictionary to another one

  ```bash
  a = dict(a=1,b=2)
  b = {'c':3}

  #  update `b` with `a`
  b.update(a)

  print(b) # {'c': 3, 'a': 1, 'b': 2}
  ```

- it doesn't overwrite prev existing values
- it does overwrite duplicate key-values
- it only updates and does not remove anything if we pass a dictionary w fewer properties
