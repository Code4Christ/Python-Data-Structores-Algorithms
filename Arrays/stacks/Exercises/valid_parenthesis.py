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
Test = Solution()

# Test Case 1
s1 = "[]"
print(f"Output : {Test.isValid(s1)}")

# Test Case 2
s2 = "([{}])"
print(f"Output : {Test.isValid(s2)}")

# Test Case 3
s3 = "[(])"
print(f"Output : {Test.isValid(s3)}")
