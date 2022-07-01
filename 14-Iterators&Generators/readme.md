## Iterator

- An object that can be iterated upon, something we can run a for loop over
- Behind the scenes, for loop calls the **next()** method and it returns the next item in the loop
  - One item at a time
  - Until it raises a _StopIteration_ error, i.e, at last item

## Iterable

- An object that returns an Iterator when iter() is called
- When we loop over something (str, list, etc.), for loop calls the iter() function on it behind the scenes and makes it into an iterator

## Generators

- Subset of iterators
- Every generator is an iterator but not vice-versa
- Easy way to create iterators
  - One way is to use _generator functions_ using **yield** keyword
  - Another way to create generators is w _generator expressions_

#### Generator Functions

- Just like a normal function but uses _yield_ instead of _return_
- Can yield multiple times unlike normal function that return only once
- Returns a generator object when invoked
- It only stores one thing at a time until it's changed any time we call the next method on it

#### Generator Expressions

- Easier way to create generators
- Look like list comprehensions for lists
- We use **()** instead of **[]**
- It's more like Tuple Comprehension in syntax

```py
g = (num for num in range(1, 10))
# g here is generator object created from generator expression
```
