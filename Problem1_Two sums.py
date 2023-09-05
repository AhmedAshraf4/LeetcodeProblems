class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        end = len(nums) - 1
        begin = 0
        while(begin < end):
            if nums[begin] + nums[end] > target:
                end -= 1
            elif nums[begin] + nums[end] < target:
                begin += 1
            else:
                break
        out = [key[begin],key[end]]
        return out
        