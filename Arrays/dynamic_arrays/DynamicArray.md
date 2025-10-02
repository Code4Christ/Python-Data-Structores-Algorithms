# Design Dynamic Array (Resizable Array)

Design a Dynamic Array (aka a resizable array) class, such as an `ArrayList` in Java or a `vector` in C++.

## Requirements
Your `DynamicArray` class should support the following operations:

- **`DynamicArray(int capacity)`**  
  Initialize an empty array with a capacity of `capacity`, where `capacity > 0`.

- **`int get(int i)`**  
  Return the element at index `i`. Assume that index `i` is valid.

- **`void set(int i, int n)`**  
  Set the element at index `i` to `n`. Assume that index `i` is valid.

- **`void pushback(int n)`**  
  Push the element `n` to the end of the array. If the array is full, resize first.

- **`int popback()`**  
  Pop and return the element at the end of the array. Assume that the array is non-empty.

- **`void resize()`**  
  Double the capacity of the array.

- **`int getSize()`**  
  Return the number of elements in the array.

- **`int getCapacity()`**  
  Return the capacity of the array.

---

## Example 1
**Input:**
```
["Array", 1, "getSize", "getCapacity"]
```
**Output:**
```
[null, 0, 1]
```

---

## Example 2
**Input:**
```
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
```
**Output:**
```
[null, null, 1, null, 2]
```

---

## Example 3
**Input:**
```
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
```
**Output:**
```
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
```

---

## Python Implementation

```python
class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        if i < self.length:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        for i in range(self.length):
            newArr[i] = self.array[i]
        self.array = newArr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
```
