# Don't forget to import re!
import re


# Define is_valid_time below:
def is_valid_time(input):
    time_regex = re.compile(r'\d\d?:\d{2}')
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False
