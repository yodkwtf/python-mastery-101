num_list = [1, 2, 3, 4]

new_dict = {num: 'even' if num%2==0 else 'odd' for num in num_list}

print(new_dict)