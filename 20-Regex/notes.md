## Regex

There are a ton of regex symbols. You can test them out in any regex editor.

They can vary a little bit based on what language you're working with.

## Rules

#### Characters

- `.` can match everything
- `\` is used to escape a string
- `\.` will only match a **.**
- `ab` will only match _ab_
- `\d` matches digit _0-9_
- `\w` matches letter, digit, or underscore

There are a bunch of cheatsheets online to refer to these rules.

The capital version of these rules reverse the rule

- `\W` gives anything that is not letter, digit or underscore
- `\D` matches anything that is not a number form 0-9

#### Quantifiers

They specify how many times something should occur in the text

- `+` matches one or more characters
- `{x}` matches exactly x times
- `{3,5}` 3 to 5 times
- `{4,}` 4 or more times
- `*` zero or more times
- `?` once or none (optional)

#### Character Classes

These are group or sets of different characters

- `[aeiou]` matches any one of the 5; if we just do `aeiou` then it'll match the exact string with these 5 letters
- `[aeiou]{2}` finds characters whenever any 2 vowels are together
- `[A-Z]` refers to all uppercase letters
- `[A-Z]{4,}` matches all words with 4 or more _uppercased_ letters
- `[^k]` matches everything that isn't _k_

#### Anchors or Boundaries

- `^` start of string or line
- `$` end of string or line
- `\b` word boundary

#### Logical Operator `|`

Allows us to write optionals strings, for example Mr. | Ms. | Mrs.

- The pipe character selects b/w the strings before and after it
- Sometimes they need to be wrapped inside parenthesis to avoid mis-matches

## Regex in Python

```py
# import re module
import re

# define a basic phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# here `r` is used to indicate that the string is a raw string so we don't need to escape the backslashes

# search a string with our regex
result = pattern.search('My number is 415 555-4242.')

result2 = pattern.findall('My number is 415 555-4242 and 888 000-3333.')

print(result.group()) # 415 555-4242
print(result2) # ['415 555-4242', '888 000-3333']
```
