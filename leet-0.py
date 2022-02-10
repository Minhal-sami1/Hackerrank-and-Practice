class Solution:
    def twoSum(nums, target):
        sum = 0
        lst = []
        cnt = 0
        for i in nums:
            if sum == target:
                return lst
            else:
                sum = 0
                if nums[i+1]:
                    sum = i + nums[i+1]
                lst.append(cnt)
                cnt += 1


test = Solution.twoSum([3, 2, 4], 6)
print(test)
