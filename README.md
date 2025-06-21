#Two_sum
 class Solution:
    def __init__(self, nums, target):
        self.nums=nums
        self.target=target
    def two_sum(self):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target) :
                    return[i, j] 
nums=list(map(int,input().strip().split()) 
target=int(input()) 
obj=Solution(nums,target) 
print(obj.two_sum())
