# LRU Cache Implementation with `OrderedDict`

This document explains the **Least Recently Used (LRU) Cache** problem, the Python implementation using `OrderedDict`, and why it is efficient.

---

## Problem Statement

**LRU Cache**

Implement the Least Recently Used (LRU) cache class `LRUCache`. The class should support the following operations:

- `LRUCache(int capacity)` → Initialize the LRU cache of size `capacity`.
- `int get(int key)` → Return the value corresponding to the key if the key exists, otherwise return `-1`.
- `void put(int key, int value)` → Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a `get` or a `put` operation is called on it.

Ensure that `get` and `put` each run in **O(1)** average time complexity.

---

### Example 1

**Input:**  
```text
["LRUCache", [2], "put", [1, 10], "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
```

**Output:**  
```text
[null, null, 10, null, null, 20, -1]
```

**Explanation:**
```python
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  # cache: {1=10}
lRUCache.get(1);      # return 10
lRUCache.put(2, 20);  # cache: {1=10, 2=20}
lRUCache.put(3, 30);  # cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      # returns 20 
lRUCache.get(1);      # return -1 (not found)
```

---

### Constraints

- `1 <= capacity <= 100`
- `0 <= key <= 1000`
- `0 <= value <= 1000`

---

## Code with Comments

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the cache as an OrderedDict to maintain insertion order
        self.cache = OrderedDict()
        # Set the maximum capacity
        self.cap = capacity

    def get(self, key: int) -> int:
        # If the key is not found in the cache
        if key not in self.cache:
            return -1
        # If the key is found, move it to the end to mark as recently used
        self.cache.move_to_end(key)
        # Return the corresponding value
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key already exists, move it to the end to mark as recently used
        if key in self.cache:
            self.cache.move_to_end(key)
        # Insert or update the value for the key
        self.cache[key] = value
        # If capacity exceeded, remove the least recently used item (first in order)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
```

---

## Why This Works

This implementation works because it leverages the **`OrderedDict`** from Python’s `collections` module, which:

- Preserves the order of insertion.
- Provides efficient methods to:
  - `move_to_end(key)` → Reorder elements to mark them as **most recently used**.
  - `popitem(last=False)` → Remove the **least recently used element**, which is always at the front.

---

### How `get()` Works
- If the key is missing → return `-1`.
- If the key exists:
  - Call `move_to_end(key)` → marks it as the most recently used.
  - Return the cached value.

👉 Ensures that every accessed item becomes the most recently used.

---

### How `put()` Works
- If the key already exists → `move_to_end(key)` so it becomes most recent.
- Update or insert the key-value pair.
- If the cache exceeds its capacity:
  - Call `popitem(last=False)` → removes the oldest/least recently used item.

👉 Guarantees that the cache size is always within the defined capacity.

---

## Example Usage

```python
# Create a cache of capacity 2
cache = LRUCache(2)

# Insert key-value pairs
cache.put(1, 1)  # Cache = {1=1}
cache.put(2, 2)  # Cache = {1=1, 2=2}

# Access key 1 (makes it most recently used)
print(cache.get(1))  # Output: 1
# Cache order = {2=2, 1=1}

# Insert a new key (capacity exceeded, remove least recently used: key 2)
cache.put(3, 3)  # Cache = {1=1, 3=3}

# Try to get key 2 (should be removed)
print(cache.get(2))  # Output: -1

# Insert another key (capacity exceeded, remove least recently used: key 1)
cache.put(4, 4)  # Cache = {3=3, 4=4}

# Check remaining keys
print(cache.get(1))  # Output: -1 (removed)
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
```

---

## Why It’s Efficient

- **Most recently used items** → at the **end** of the `OrderedDict`.
- **Least recently used items** → at the **beginning**.
- Operations are constant time:
  - `get()` → O(1) (dict lookup + reordering).
  - `put()` → O(1) (insert/update + possible eviction).

This matches the requirements of an LRU cache, making it optimal for real-world use and interview scenarios.
