# import re module
import re

# define a basic phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# here `r` is used to indicate that the string is a raw string so we don't need to escape the backslashes

# search a string with our regex
result = pattern.search('My number is 415 555-4242.')

result2 = pattern.findall('My number is 415 555-4242 and 888 000-3333.')

print(result.group())
print(result2)
