## Lists

- are data structures to store other different data type collections
- there are a whole lot of methods for lists

---

## List Methods

- `append` - inserts a new item at the end
- `extend` - inserts the given items(or a new list) at the end and extends the original one
- `insert` - inserts an item at the specified index
- `clear` - removes all the items from the list
- `pop` - removes and returns an item from the given index (by default removes from the last)
- `remove(x)` - removes the first instance of the given item
- `index(x)` - returns the index of the specified item
- `count` - returns how many times an item occurs in a list
- `reverse` - reverses the list w/o creating a new one
- `sort` - sorts item based on asc order
- `join` - technically a string method but is used to combine/concatenate items of a list
  ```bash
  words = ["Coding", "is", "fun!"]
  text = " ".join(words) # joins the words with a space
  print(text)
  ```

---

## List Comprehension

- does a specific task for every iteration when looping over a list and it creates a new list
  ```bash
  nums = [1, 2, 3]
  # create a new list where the items are doubles
  doubled_nums = [num*2  for num in nums]
  print(doubled_nums)
  ```
- technically, we can do the same using loops but that'd be a bit tedious
- used a lot with data science, web deb, etc.

#### LS with Conditional Logic

```bash
numbers = [1,2,3,4,5,6]

# store even values
evens = [num for num in numbers if num % 2 == 0] # [2,4,6]

# if even, double it and if odd, half it
weird = [num*2 if num%2==0 else num/2 for num in numbers] # [.5, 4, 1.5, 8, 2.5, 12]
```

---

## Nested Lists

- lists inside lists
- used a lot in almost all of the fields

  ```
  nested_list = [[1,2,3], [4,5,6], [7,8,9]]

  print(nested_list[0][1]) #2
  print(nested_list[1][-1]) #6
  ```

- we'll have to use nested loops to iterate over these

- List Comprehension in Nested Loop
  ```
  empty_board = [['x' for x in range(1,4)] for n in range(1,4)]
  print(empty_board)
  ```
