#162. Find Peak Element
#O(LogN)
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if (mid == len(nums)-1 or nums[mid+1]<nums[mid]) and (mid ==0 or nums[mid]>nums[mid-1]):
                return int(mid)
            elif nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1