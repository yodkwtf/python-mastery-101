## Tuple

- Ordered collection of items `(item1, item2)`
- it is immutable and cannot be changed
- we can also have nested tuples

##### WHY USE THEM?

- they are faster if you don't mind immutability
- makes code safer, value doesn't get changed
- can act as valid keys in dict, unlike lists
- some methods return tuples
- An example for using tuple in a real case can be days of a week

  ```bash
  days = tuple(monday, tuesday, wednesday, thursday, friday, saturday, sunday)

  # access data with index
  print(days[0]) # monday
  ```

##### TUPLE METHODS

- `count(item)` - returns how many times the specified item is in tuple
- `index(item)` - returns the index of the specified item's first instance

---

---

## Sets

- just like mathematical sets, created by `{}`
- cannot have duplicate values
- are unordered, hence can't be access by index

  ```python
  # defining sets
  s = {1, 2, 3}

  s2 = set({4, 5, 6})
  ```

##### WHY USE THEM?

Suppose I have 100 people coming from a lot of cities and we want to find the unique cities. We can create a set out of the list of cities.

```python
projects = ['java', 'HTML', 'python', 'java', 'css', 'python']

# finding unique stack
stack = set(projects)
```

##### SET METHODS

- `add(item)` - adds item to the set; ignores if item is already there
- `remove(item)` - removes item; throws error if item isn't there
- `discard(item)` - removes item; doesn't throw error if item isn't there
- `copy()` - creates a copy of the set
- `clear()` - removes all the items from the set
- There are many mathematical methods with sets like union and intersection

#### Set Comprehension

- same stuff as we have for list and dict comprehension
- useful when we convert other data types into set to get unique instances

  ```py
  s = {x **2 for x in range(5)}
  print(s) # {0, 1, 4, 9, 16}

  print({letter for letter in "hello"}) # {'h', 'o', 'l', 'e'}

  ```
