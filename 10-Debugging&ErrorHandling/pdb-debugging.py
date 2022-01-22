first = "First"
second = "Second"

import pdb; pdb.set_trace() # stops execution below this point

result = first + second
third = "Third"
result += third

print(result)

## Using pdb 
# import pdb
# pdf.set_trace() 

# or

# import pdb; pdb.set_trace()

## Common PDB Commands: 
# l (list) -> lists where we are in our code execution
# n (next line)  -> moves the debugger to next line
# p (print) -> prints the variable value next to it
# q (quit) -> but quits in a ugly way
# c (continue - finishes debugging)