# Implement your is_all_strings function below:
def is_all_strings(li):
    return all(type(item)== str for item in li)

print(is_all_strings(['a', 'b']))