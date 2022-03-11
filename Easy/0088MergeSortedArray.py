class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, r = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 < 0 or nums1[p1] <= nums2[p2]:
                nums1[r] = nums2[p2]
                p2 -= 1
            else:
                nums1[r] = nums1[p1]
                p1 -= 1
            r -= 1
            
            
