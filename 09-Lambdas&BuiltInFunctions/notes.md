## Lambdas

- lambdas are single line functions that have no name
- sometimes are called anonymous functions
- only has a single expression w/o the return keyword
- the result can be stored in a variable but not so common use

  ```py
  add = lambda a, b: a + b

  print(add(3,10)) # 13
  ```

- they are not used that much

---

## Map

- a standard built-in function
- takes 2 arguments - a function(lambda) and an iterable
- runs the passed function for each iterable and returns a collection called _map object_

```py
nums = [2,4,5,6,8]

doubles = map(lambda n: 2*n, nums)

print(doubles) # <map object at 0x000001B8AF75EDA0>
print(list(doubles)) # [4, 8, 10, 12, 16]
```

- this is one of the common use case of lambdas
- it returns a map object which needs to be converted into list to print it
- however, the map object is iterable

---

## Filter

- it basically filters out values out of a collection based on the lambda
- takes 2 argument, a function (usually lambda) and an iterable collection
- runs lambda for each iterable and returns a collection called _filter object_
- filter object only the values that return true to the lambda

```py
# Filter out the evens from the list
nums = [1, 2, 3, 4, 5]

even_nums = filter(lambda n: n % 2 == 0, nums)

print(even_nums) # <filter object at 0x000001B978C0EDD0>
print(list(even_nums)) # [2, 4]
```

- whenever we use lambda with filter, lambda needs to be a boolean expression (should return True/False)

#### Things to Remember?

We can use **map** and **filter** together to create some complex functionality.

In most cases, we can achieve the same output as map and filter using list comprehensions and it's perfectly okay to use that.
It's just good to know these things exist too.

We might see the lambda way in certain external libraries so it's good to know.

---

## Built-In Functions

#### all() & any()

**all** - Returns true if all elements of iterable are truthy (or if the iterable is empty)

```py
print(all([0,1,3,4])) # False since 0 is falsy

names = ["John", "Jack", "Jay"]
is_J_first = [name[0]=="J" for name in names]

print(is_J_first) # [True, True, True]
print(all(is_J_first)) # True
```

**any** - Returns true if any one of the iterable is truthy

```py
print(any([0, '', 4, None])) # True, since 4 is truthy
```

> When iterating over lists, we can avoid using list comprehensions when we're using `any` or `all` method and it'll work the same way. Incase we need the results for later use then using list comprehension would make good sense.

#### sorted()

- Returns a new sorted _list_ from the items in iterable
- Works on anything that is iterable

```py
numbers = [6, 12, 15, 11]

print(sorted(numbers)) # [6, 11, 12, 15]
print(sorted(numbers, reverse=True)) # [15, 12, 11, 6]
```

- Unlike the `sort` list method, it doesn't actually modify the list

#### max() and min()

**max** - Returns the largest item in an iterable or the largest b/w 2 or more passed arguments

**min** - Returns the smallest item from an iterable or b/w the passed arguments

```py
max(3, 99, 67) # 99
min(3, 99, 67) # 3

max('c', 'd', 'a') # 'd'
min('c', 'd', 'a') # 'a'

max("hello world") # 'w'
min("hello world") # ' '
```

#### reversed()

Reverses any iterator but returns a _reversed object_ and not a list

```py
for letter in reversed("hello"):
  print(letter) # 'o' 'l' 'l' 'e' 'o'

# using slice
print("hello"[::-1]) # 'olleh'

# doing above with reversed
rev = "".join(list(reversed("hello")))
print(rev) # 'olleh'
```

- Unlike the reverse list method it does not actually modify the iterator

#### len()

- Pretty basic, right? It returns the length of an object. List, string, tuple, dictionary (counts the np. of keys), you name it!
- BTS, len uses a dunder (*d*ouble *under*score) method called **\_\_len\_\_()**
  ```py
  'hello'.__len__() # 5
  ```
- We are not supposed to directly call this method but using this we can create our methods for our classes

#### abs(), sum(), & round()

**abs** - returns the absolute value of a number which can either be an integer or a floating point number

```py
abs(-25) #25
abs(-75/8) #9.375
abs(2.5) #2.5
abs('20') # ERROR
```

**sums** - takes an iterable with an optional _start_ argument and returns the total sum of start and all the items of iterable (left to right)

The default value of the _start_ argument is 0.

```py
sum([1, 2, 3]) # (1+2+3) = 6
sum([1, 2, 3], 10) # 10 + (1+2+3) = 16
sum([1, 2, 3], -11) # -11 + (1+2+3) = -5
```

**round** - returns number with _n digits_ after the decimal as specified. If not specified, it rounds off to the nearest integer.

```py
round(10.2) # 10
round(-5.6) # -6
round(75/7) # 11
round(75/7, 3) # 10.714
```

#### zip

- Zips and returns the given iterators into a single collection called _iterator of tuples_
- In the iterator of tuples, first element will be a tuple of first element of all the iterators passed in the zip function (see code below)

```py
first_zip = zip([1, 2, 3], [4, 5, 6])

first_zip # <zip object at 0x000002257C54B100>

list(first_zip) # [(1,4), (2,5), (3,6)]
dict(first_zip) # {1:4, 2:5, 3:6}
```

- It stops zipping as soon as the shortest iterable runs out of the elements
- **eg** - If n1 has 5 elements & n2 has 8 elements and they are zipped, the result iterator will only have 5 elements

- We are not limited to just use numbers, we can even combine strings and anything else

We can also unpack a list inside a zip function

```py
three_by_two = [(0,1), (1,2), (2,3)]

z = list(zip(*three_by_two))
# z = list(zip((0,1), (1,2), (2,3)))
# z = [(0, 1, 2), (1, 2, 3)]
```

In the above code `*` is unpacking the list _three_by_two_ and taking out all of the tuples from it to pass them individually inside the zip function

> All of these methods need not be remembered. They are just one google search away.
