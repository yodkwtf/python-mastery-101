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
