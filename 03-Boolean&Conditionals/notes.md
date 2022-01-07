## Input Function

- Gets an input from users
- Built-in function
- Result is always a string
- a msg can be passed inside for the user

---

## Conditional Statements (If-Else)

- use `if-else` statements to make the program do different things based on some logic/condition
- we can do a lot more than just print stuff inside `if-else`
- we can avoid elif and else statements too based on our needs
- we will only have one `if` and one `else` but we can have as many `elif`'s as we want

#### Comparison Operators

- there are many comparison operators - `>, <, >=, <=, !=, ==`
- all of the comparison operators return True or False

#### Truthiness and Falseness

- All conditionals resolve True or False
- False values are - empty objects, empty strings, None, and zero

#### Logical Operators

- used to combine comparison operators to create boolean logic
- 3 types - `AND, OR, NOT`
- AND - Truthy when all the conditions are true
- OR - Truthy when any one of the conditions are true
- NOT - Truthy when opposite of the given condition is true

#### is vs. "=="

- they are very similar too

  ```bash
  a = 1
  a == 1 #true
  a is 1 #true
  ```

- They are different as `is` compares the instance and not the value

  ```bash
  a = [1, 2, 3]
  b = [1, 2, 3]

  a == b # True (same value?, yes)
  a is b # False (same instance?, no)

  c = b
  c is b # True (they're both pointing to the same thing in memory)
  ```

- `is` is only true when 2 values reference the same item in memory
