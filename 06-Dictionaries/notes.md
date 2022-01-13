## Dictionaries

- Are used to describe data in more detail
- Data structure that consists key-value pairs
- `keys` are used to describe data and `values` are used to represent data
- `keys` are usually num or strings but `values` can be anything from boolean to nested dictionaries

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
