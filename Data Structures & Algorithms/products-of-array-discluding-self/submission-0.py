class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        # for i,j in enumerate( range(len(nums))):
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if i==j:
                    continue
                mul=mul*nums[j]
            res.append(mul)
        return res
