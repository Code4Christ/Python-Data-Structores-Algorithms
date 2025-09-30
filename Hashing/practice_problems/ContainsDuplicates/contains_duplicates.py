from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        countMap = {}
        # For every number in the numbers list
        for num in nums:
            # if the number is not found in the hashmap
            if num not in countMap:
                print(num)
                # add the number to the hash map with a value of 1
                countMap[num] = 1
            # otherwise, if the number is already in the hash map
            else:
                # return True because we have now found a duplicate
                return True
        # If we get to the end of the for loop and find no duplicates, return false
        return False
    
solution = Solution()

print(f"Case #1 {solution.containsDuplicate([1,2,3,1])}")
print(f"Case #2 {solution.containsDuplicate([1,2,3,4])}")
print(f"Case #3 {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")
