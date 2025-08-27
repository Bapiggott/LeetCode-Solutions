class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found =  {}
        for i, num in enumerate(nums):
            opposite = target - num
            if opposite in found:
                return [found[opposite], i]
            else:
                found[num] = i

