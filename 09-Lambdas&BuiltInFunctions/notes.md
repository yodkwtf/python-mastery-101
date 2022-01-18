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
