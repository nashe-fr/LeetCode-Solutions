class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        

        #have hashtable to store all previous numbers
        seen = {}
        #if target - current number = s in hash
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
        #answer = s index, current index 
                return [seen[diff],i]
        #else, store the current number and its index
            seen[n]=i
        return

