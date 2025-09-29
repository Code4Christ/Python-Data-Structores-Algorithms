from typing import List

## My Solution at O(n^2)
print('''\n
MY SOLUTION
''')
class Solution1:
    def removeElementCustom(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            print("nums after remove ", nums)

        return len(nums)

solution = Solution1()

nums = [1,1,2,3,4]
val = 1
print(solution.removeElementCustom(nums, val))

## TWO POINTER SOLUTION AT O(n)
print('''\n
TWO POINT SOLUTION      
''')
class Solution2:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution2() 
nums = [1,1,2,3,4]
val = 1
print(solution.removeElement(nums, val))