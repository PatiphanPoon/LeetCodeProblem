class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = dict()
        for i in nums:
            if i in check:
                return True
            else:
                check[i] = True      
        return False
                
