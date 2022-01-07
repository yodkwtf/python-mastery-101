## Variables

- Store values/data to access them later
- They can store all sorts of data types
- They need to be assigned before they can be used
- Variables can be assigned to other variables
  ```bash
   a = 10
   b = a
  ```
- Can be reassigned at any time
  ```bash
  a = 10
  a = 50
  ```
- Can be assigned at the same time as other variables
  ```bash
    a, b, c = 10, 25, 50
  ```

##### Rules for naming Variables

- have to start with letter or underscore only
- name must contain letters, numbers, or underscores
- names are case sensitive

##### Naming Conventions for Variables

- should be named using snake_case
- usually should be lowercase
- CAPITAL_CAME_CASE refers to constants like pi(3.14)
- UpperCamelCase refers to classes
- variables with double underscore should be left alone and shouldn't be messed with - `__no_touch__`

---

#### Data Types

- any assigned values must be a valid data type
- there are many `int`, `float`, `str`, `boolean`, `list`, `dict` and much more

#### Data Type Conversion

- data types can be converted from one form to another
  ```
  decimal = 3151.15155
  integer = int(decimal)
  # integer now equals to 3151
  ```

---

## Strings

- any character, symbol, word or letter
- any valid Unicode character
  ```
  some_string = 'My name is Durgesh'
  ```
- can be declared with either single or double quotes (just try to stay consistent)

##### Escape Sequences

- special sequences used inside strings to do special task via python
- can be used to escape quotes when we have quotes inside quotes
- many more in the docs

##### String Concatenation

- used to combine multiple strings together
- can be done using `+` operator in python

##### Formatting Strings

- called F-strings, used to interpolate things
- converts `int` into strings when written inside unlike concatenation

##### String Indexes

- can be used to access a particular character from a string using `[]`
- indexes are 0 based
- can be accessed using negative numbers as well

---

#### Dynamic Typing vs Statically Typed

Python is dynamically typed language. You can reassign a variable to different data types which isn't the case for many other languages.

C++, for example is statically typed where if we define a variable as boolean, it has to stay boolean otherwise there will be an error

---

#### None

- Python's version of **null**
- Represnets nothingness
- Used when we want a variable declared but don't have anything to assign to it just yet
