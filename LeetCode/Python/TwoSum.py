class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index =[]
        l = len(nums)
        for i in range(0,l):
            find = target - nums[i]
            for j in range(i+1,l):
                if nums[j] == find:
                    index.append(i)
                    index.append(j)
                    break
            
        return index
