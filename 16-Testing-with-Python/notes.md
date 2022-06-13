## Testing

Done to test whether block of code is running well or throwing errors

#### Why Test?

- Reduce bugs in code
- Ensures that your bugs stay fixed
- Ensure new features don't break old ones

Writing tests can slow you down. It's not necessary to have them for all your projects - big or small. It's more up to personal preference.

It's a good idea to write them you have a large scale project with customers. clients, multiple developers, etc. depending and working on it.

## Test Driven Development (TDD)

- Tests are written first
- Then write code to make those tests pass
- Once tests pass, the feature is complete
- Just one of the way to write tests, you can change the order as per your preference

#### "Red, Green, Refactor" Way

It's a just mantra that people follow while doing TDD

1. Red - Write a test that fails
2. Green - Write the minimal amount of code to pass test
3. Refactor - Clean up code, while ensuring tests still pass

## Assertions

- `assert` keyword accepts an expression to check if it's true
- Raises an _AssertionError_ if expression is falsy
- Returns _None_ if expression is truthy
- Accepts option error msg as second argument

```py
def add_positive_nums(x,y):
  assert x > 0 and y > 0, "Both the numbers must be positive"
  return x+y

print(add_positive_nums(2, 5)) # 7
add_positive_nums(3, -5) # AssertionError: Both the numbers must be positive
```

If a Python file is run with the **-O** flag assertions will not be evaluated.

Therefore don't make your code dependent on assertions as they can be ignored.

## doctests

- allows us to write tests inside doc strings
- we have to write code in a certain way like inside of a REPL
- if we write tests this way, it can also work as a documentation for other devs along with being a test
- there's a special command to run the doctests w/o having to evaluate anything

```bash
python -m doctest -v file_name.py
```

This will show all the tests that ran, expected output, actual output, no. of passed and failed tests.

- We have to be really careful while mentioning expected output inside doctests. Things like quotation marks, empty spaces, list (or dict) order, etc. can really be a pain at times.

## Unit Tests

Unit testing is a technique where we test small individual components (units) as we go

#### unittest

- Module used for this that comes with a lot of built in assertions
- Unit tests can be written as classes that inherit from `unittest.TestCase`
- This gives us a lot of assertions
- Tests are run by calling `unittest.main()`

There are a bunch of different assertions method provided by the module. We can refer to the documentation for more info about them.

#### _setUp_ & _tearDown_

- **setUp** - A function used to run something before every test
- **tearDown** - A function used to run something after every test
- Names are really imp and should be the same
