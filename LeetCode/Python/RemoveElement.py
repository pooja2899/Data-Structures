class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if all(ele == nums[0] for ele in nums) and nums[0] == val:
            return 0
        
        last = len(nums)-1
        
        while(nums[last]==val):
                last -= 1
        
        i = 0
        while(i!=last and i<last):
            if nums[i]==val:
                x = nums[last]
                nums[last] = nums[i]
                nums[i] = x
                last = last - 1
                while(nums[last]==val):
                    last -= 1
            i = i + 1
                
        return last+1
