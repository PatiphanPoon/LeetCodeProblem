class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = dict()
        st = [0]
        ans = []
        
        for i in range(1, len(nums2)):
            if nums2[i] > nums2[i - 1]:
                while st and nums2[st[-1]] < nums2[i]:
                    table[nums2[st.pop()]] = nums2[i]
            st.append(i)
        while st:
            table[nums2[st.pop()]] = -1
        
        for i in nums1:
            ans.append(table[i])
        return ans
