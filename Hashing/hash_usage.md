# Hash Usage

Having talked about **TreeSets** and **TreeMaps** in the previous chapter, let's discuss how the map and the set interfaces can be implemented using hashing.

In this lesson, we will be focusing on the usage of a **HashSet** and a **HashMap**, but we will cover their implementation in the next lesson. While knowing the implementation is important, it is not as important as knowing how to use them.

Hash maps are probably one of the most useful data structures/concepts for coding interviews. When questions use the words *"unique"*, *"count"*, or *"frequency"*, it is almost certain a hashmap or hashset will be useful for solving the problem.

Recall that the difference between a set and a map is that:
- **Sets** contain *keys only*.  
- **Maps** contain *key-value pairs*.  

---

## Motivation

Let's start off by comparing **hash maps** to **tree maps** and **sorted arrays** and understand what trade-offs we make using each data structure.

| Operation        | TreeMap   | HashMap (avg case) | Array                |
|------------------|-----------|---------------------|----------------------|
| Insert           | O(log n)  | O(1)                | O(n)                 |
| Remove           | O(log n)  | O(1)                | O(n)                 |
| Search           | O(log n)  | O(1)                | O(log n) if sorted   |
| Inorder Traversal| O(n)      | -                   | -                    |

The time complexity listed for hash maps is the **average case time complexity**. However, it is widely accepted in most cases, including interviews, to assume **constant time complexity**.

---

## Tree Maps vs Hash Maps

The downside of hash maps is that they are **not ordered**, so it is not possible to traverse the keys of a hashmap in any particular order. If you were to iterate through all the keys, you would first need to **sort them**, which will run in **O(n log n)** time, making it slower than an inorder traversal of a tree map (**O(n)**).

Because hashmaps don't allow duplicates and have key-value pairs, we can use them to **count frequency of keys**.

---

## Example: Counting Frequencies

Given the array:

```python
["alice", "brad", "collin", "brad", "dylan", "kim"]
```

We can add all the elements into a hash map as keys. If a name already exists in our hash map, we increment its value by 1. Otherwise, we set it to 1.

| Key    | Value |
|--------|-------|
| Alice  | 1     |
| Brad   | 2     |
| Collin | 1     |
| Dylan  | 1     |
| Kim    | 1     |

### Python Example

```python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1
```

---

## Time and Space Complexity

**Time:**  
- With a tree map → insertion = O(log n), total = O(n log n)  
- With a hash map → insertion = O(1), total = O(n)  

**Space:**  
- Hash map uses O(n), where *n* is the number of unique keys.
