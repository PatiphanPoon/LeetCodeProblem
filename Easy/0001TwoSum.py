class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in di and di[dif] != i:
                return [i, di[dif]]
