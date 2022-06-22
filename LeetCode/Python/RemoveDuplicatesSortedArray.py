class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        length = 1
        previous = nums[0]
        index = 1
        for i in range(len(nums)):
            if nums[i]!=previous:
                length = length + 1
                previous  = nums[i]
                nums[index] = nums[i]
                index += 1
        return length
