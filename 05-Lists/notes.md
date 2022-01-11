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
