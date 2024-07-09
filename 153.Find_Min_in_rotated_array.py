#153 Find Minimum in Rotated Sorted Array
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low =0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2    
            if nums[low]<=nums[high]:
                return nums[low]
            elif nums[low]<=nums[mid]:
                low =mid+1
            else:
                high =mid
