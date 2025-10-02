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


# ------------------------------
# LeetCode-style driver
# ------------------------------

def run_operations(ops, inputs):
    results = []
    obj = None

    for op, inp in zip(ops, inputs):
        if op == "Array":  # constructor
            obj = DynamicArray(inp[0])
            results.append(None)
        elif op == "get":
            results.append(obj.get(inp[0]))
        elif op == "set":
            obj.set(inp[0], inp[1])
            results.append(None)
        elif op == "pushback":
            obj.pushback(inp[0])
            results.append(None)
        elif op == "popback":
            results.append(obj.popback())
        elif op == "getSize":
            results.append(obj.getSize())
        elif op == "getCapacity":
            results.append(obj.getCapacity())

    # Replace Python None with "null" to match LeetCode output
    return ["null" if r is None else r for r in results]

# Example 1
ops1 = ["Array", "getSize", "getCapacity"]
inputs1 = [[1], [], []]
output1 = run_operations(ops1, inputs1)
print("Example 1 Output:", output1)  # Expected: ['null', 0, 1]


# Example 2
ops2 = ["Array", "pushback", "getCapacity", "pushback", "getCapacity"]
inputs2 = [[1], [1], [], [2], []]
output2 = run_operations(ops2, inputs2)
print("Example 2 Output:", output2)  # Expected: ['null', 'null', 1, 'null', 2]


# Example 3 from the prompt
ops3 = ["Array", "getSize", "getCapacity", "pushback", "getSize", "getCapacity",
    "pushback", "getSize", "getCapacity", "get", "set", "get", "popback",
    "getSize", "getCapacity"]
inputs3 = [[1], [], [], [1], [], [], [2], [], [], [1], [1, 3], [1], [], [], []]

output3 = run_operations(ops3, inputs3)
print("Example 3 Output:", output3)  # Expected: ['null', 0, 1, 'null', 1, 1, 'null', 2, 2, 2, 'null', 3, 3, 1, 2]