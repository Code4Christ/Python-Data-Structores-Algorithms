# Array Operations in Python (Simulating Fixed-Size Arrays)

This document explains some basic operations on a fixed-size array using Python lists.  
We use `length` to track the number of actual elements (“real values”) in the array, and `capacity` to represent the total size of the underlying array (memory allocated).

---

## Code Explanation

```python
# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
```

- **Purpose:** Adds a value `n` to the **end of the array** if there is space.  
- **Parameters:**  
  - `arr`: underlying array  
  - `n`: value to insert  
  - `length`: current number of elements  
  - `capacity`: maximum allowed elements  
- **Behavior:** Only inserts if the array is not full.

---

```python
# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
```

- **Purpose:** Removes the last element from the array.  
- **Behavior:** Sets the last “real” value to a default (0) and conceptually decreases `length`.  
- **Note:** In practice, `length` would need to be updated by the caller.

---

```python
# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n
```

- **Purpose:** Inserts a value `n` at a specific index `i`.  
- **Behavior:** Shift elements right and insert `n`.  

---

```python
# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
```

- **Purpose:** Deletes the element at index `i`.  
- **Behavior:** Shift elements left to overwrite the removed element.  

---

```python
def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])
```

- **Purpose:** Prints all elements in the array up to its capacity.

---

## Summary

| Function         | Purpose |
|-----------------|---------|
| `insertEnd`      | Append a value to the end of the array if space allows |
| `removeEnd`      | Remove the last element of the array |
| `insertMiddle`   | Insert a value at a given index, shifting elements right |
| `removeMiddle`   | Remove a value at a given index, shifting elements left |
| `printArr`       | Print all elements in the array up to capacity |

- `length` tracks actual elements.  
- `capacity` is the fixed allocated size.  
- Shifting elements is required for middle inserts/removes.  
