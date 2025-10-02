# Dynamic Arrays

Dynamic Arrays are a much more common alternative to static arrays. They are useful because they can grow as elements are added. In JavaScript and Python, these are the default arrays.

Unlike static arrays, with dynamic arrays we don’t have to specify a size upon initialization.

In different languages, dynamic arrays may be assigned a default size – Java being `10` and C# being `4`. Regardless, these are automatically resized at runtime as the arrays grow.

## Dynamic Array Insertion

When inserting at the end of a dynamic array, the next empty space is found and the element is inserted there. Consider an array of size `3` where we push elements into it until we run out of space.

```python
# Insert n in the last position of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()
        
    # insert at next empty position
    self.arr[self.length] = n
    self.length += 1
```

## Resize

Since the array is dynamic in size, we can continue to add elements. But it's not magic, this is achieved by copying over the values to a new static array that is double the size of the original. This means that the resulting array will be of size `6` and will have new space allocated for it in memory. The following visual and code demonstrates this resize operation.

```python
def resize(self):
    # Create new array of double capacity
    self.capacity = 2 * self.capacity
    newArr = [0] * self.capacity 

    # Copy elements to newArr
    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr
```

When all the elements from the first array have been copied over, the first static array will be deallocated.  
Adding elements to a dynamic array runs in `O(1)` amortized time.

Amortized time complexity is the average time taken per operation over a sequence of operations. The resize operation itself is `O(n)`, but since it is not performed every time we add an element, the average time taken per operation is `O(1)`. But this is only the case if we double the size of the array when we run out of space.

### Why double the capacity?

The visual below shows a resulting array of size `8`. Now imagine that we wanted to dynamically fill it up and we started with a size `1` array. We would add `5`, double the space to add `6`, double that space to add `7` and `8`, double that space to add `9`, `10`, `11`, and `12`.

The size of the above array went from `1 -> 2 -> 4 -> 8`.

To analyze the time complexity we have to take into consideration the sum of all the operations that occurred before the last one since we would not have gotten to the resulting array without these operations. To achieve an array of size `8`, we would have to perform `1 + 2 + 4 + 8 = 15` operations, which includes the resize operations.

The pattern here is that the last term (the dominating term) is always greater than or equal to the sum of all the terms before it. In this case, `1 + 2 + 4 = 7`, and `7 < 8`. Add in the `8` to the `7`, we get a total of `15` operations to create the resulting array of size `8`.

Generally, the formula is that for any array size `n`, it will take at most `2n` operations to create, which would belong to `O(n)`.

Since inserting `n` elements into a dynamic array is `O(n)`, the amortized time complexity of inserting a single element is `O(1)`.

With time complexity, we are concerned with asymptotic analysis. This means we care about how quickly the runtime grows as the input size grows. We don't distinguish between `O(2n)` and `O(n)` because the runtime grows linearly with the input size, even if the constant is doubled. With time complexity analysis, we typically drop constant terms and coefficients.

## Other Operations

Inserting or removing from the middle of a dynamic array would be similar to a static array. We would have to shift elements to the right or left to make space for the new element or to fill the gap left by the removed element. This would run in `O(n)` time.

## Time Complexity

| Operation | Big-O Time | Notes |
|-----------|------------|-------|
| Access    | O(1)       | Direct access by index |
| Insertion | O(1)*      | O(n) if insertion in the middle since shifting will be required |
| Deletion  | O(1)*      | O(n) if deletion in the middle since shifting will be required |





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
