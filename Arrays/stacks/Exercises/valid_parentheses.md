# Valid Parentheses

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.  
2. Open brackets are closed in the correct order.  
3. Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

## Examples

**Example 1:**

```
Input: s = "[]"
Output: true
```

**Example 2:**

```
Input: s = "([{}])"
Output: true
```

**Example 3:**

```
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.
```

## Constraints

- 1 <= s.length <= 1000

## Solution (Incorrect Approach)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == '(':
            success = ')'
        if s[0] == '{':
            success = '}'
        if s[0] == '[':
            success = ']'

        if s[-1] == success:
            return True
        else:
            return False
```

**Note:** This solution only checks if the first and last characters are matching brackets. It does **not** correctly solve the general valid parentheses problem.
